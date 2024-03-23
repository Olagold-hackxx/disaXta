# Copyright 2022 Cartesi Pte. Ltd.
#
# SPDX-License-Identifier: Apache-2.0
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License. You may obtain a copy of the
# License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

import json
from datetime import datetime
from urllib.parse import parse_qs, urlparse

import donation.wallet as Wallet
from donation.donator import Donatee
from donation.encoders import BalanceEncoder
from donation.log import logger
from donation.model import DisasterReport
from donation.outputs import Error, Log
from donation.util import hex_to_str
from routes import Mapper


class DefaultRoute:

    def execute(self, match_result, request=None):
        return Error("Operation not implemented")


class AdvanceRoute(DefaultRoute):

    def _parse_request(self, request):
        self._msg_sender = request["metadata"]["msg_sender"]
        self._msg_timestamp = datetime.fromtimestamp(request["metadata"]["timestamp"])
        request_payload = json.loads(hex_to_str(request["payload"]))
        self._request_args = request_payload["args"]

    def execute(self, match_result, request=None):
        if request:
            self._parse_request(request)


class WalletRoute(AdvanceRoute):

    def __init__(self, wallet: Wallet):
        self._wallet = wallet


class DepositERC20Route(WalletRoute):

    def execute(self, match_result, request=None):
        return self._wallet.erc20_deposit_process(request)


class DepositERC721Route(WalletRoute):

    def execute(self, match_result, request=None):
        return self._wallet.erc721_deposit_process(request)


class BalanceRoute(WalletRoute):

    def execute(self, match_result, request=None):
        account = match_result["account"]
        balance = self._wallet.balance_get(account)
        return Log(json.dumps(balance, cls=BalanceEncoder))


class WithdrawErc20Route(WalletRoute):

    def execute(self, match_result, request=None):
        super().execute(match_result, request)
        return self._wallet.erc20_withdraw(
            self._msg_sender,
            self._request_args.get("erc20").lower(),
            self._request_args.get("amount"),
        )


class TransferErc20Route(WalletRoute):

    def execute(self, match_result, request=None):
        super().execute(match_result, request)
        return self._wallet.erc20_transfer(
            self._msg_sender,
            self._request_args.get("to").lower(),
            self._request_args.get("erc20").lower(),
            self._request_args.get("amount"),
        )


class WithdrawErc721Route(WalletRoute):

    def __init__(self, wallet):
        super().__init__(wallet)
        self._rollup_address = None

    @property
    def rollup_address(self):
        return self._rollup_address

    @rollup_address.setter
    def rollup_address(self, value):
        self._rollup_address = value

    def execute(self, match_result, request=None):
        super().execute(match_result, request)
        if self._rollup_address is None:
            return Error(
                "DApp Address is needed to end an Donation. Check Dapp documentation on how to proper set the DApp Address"
            )
        return self._wallet.erc721_withdraw(
            self._rollup_address,
            self._msg_sender,
            self._request_args.get("erc721").lower(),
            self._request_args.get("token_id"),
        )


class TransferErc721Route(WalletRoute):
    def execute(self, match_result, request=None):
        super().execute(match_result, request)
        return self._wallet.erc721_transfer(
            self._msg_sender,
            self._request_args.get("to").lower(),
            self._request_args.get("erc721").lower(),
            self._request_args.get("token_id"),
        )


class DonationRoute(AdvanceRoute):

    def __init__(self, donatee):
        self._donatee: Donatee = donatee


class CreateDonationRoute(DonationRoute):

    def _parse_request(self, request):
        super()._parse_request(request)
        self._request_args["erc20"] = self._request_args["erc20"].lower()
        erc721 = self._request_args["item"]["erc721"].lower()
        self._request_args["item"] = DisasterReport(
            erc721, self._request_args["item"]["token_id"]
        )
        self._request_args["start_date"] = datetime.fromtimestamp(
            self._request_args["start_date"]
        )
        self._request_args["end_date"] = datetime.fromtimestamp(
            self._request_args["end_date"]
        )

    def execute(self, match_result, request=None):
        super().execute(match_result, request)
        return self._donatee.donaion_create(
            self._msg_sender,
            self._request_args.get("disaster_report"),
            self._request_args.get("erc20"),
            self._request_args.get("title"),
            self._request_args.get("description"),
            self._request_args.get("amount"),
            self._request_args.get("start_date"),
            self._request_args.get("end_date"),
            self._msg_timestamp,
        )


"""
class EndDonationRoute(DonationRoute):

    def __init__(self, donator):
        super().__init__(donator)
        self._rollup_address = None

    @property
    def rollup_address(self):
        return self._rollup_address

    @rollup_address.setter
    def rollup_address(self, value):
        self._rollup_address = value

    def execute(self, match_result, request=None):
        super().execute(match_result, request)
        if self._rollup_address is None:
            return Error(
                "DApp Address is needed to end an Donation. Check Dapp documentation on how to proper set the DApp Address"
            )
        return self._donatee.donation_end(
            self._request_args.get("donation_id"),
            self._rollup_address,
            self._msg_timestamp,
            self._msg_sender,
            self._request_args.get("withdraw", False),
        )
"""


class InspectRoute(DefaultRoute):

    def __init__(self, donatee):
        self._donatee: Donatee = donatee


class Router:

    def __init__(self, wallet, donator):
        self._controllers = {
            "erc20_deposit": DepositERC20Route(wallet),
            "erc721_deposit": DepositERC721Route(wallet),
            "balance": BalanceRoute(wallet),
            "erc721_withdraw": WithdrawErc721Route(wallet),
            "erc721_transfer": TransferErc721Route(wallet),
            "erc20_withdraw": WithdrawErc20Route(wallet),
            "erc20_transfer": TransferErc20Route(wallet),
        }

        self._route_map = Mapper()
        self._route_map.connect(
            None, "erc20_deposit", controller="erc20_deposit", action="execute"
        )
        self._route_map.connect(
            None, "erc721_deposit", controller="erc721_deposit", action="execute"
        )
        self._route_map.connect(
            None, "balance/{account}", controller="balance", action="execute"
        )
        self._route_map.connect(
            None, "erc721withdrawal", controller="erc721_withdraw", action="execute"
        )
        self._route_map.connect(
            None, "erc20withdrawal", controller="erc20_withdraw", action="execute"
        )
        self._route_map.connect(None, "end", controller="donation_end", action="execute")
        self._route_map.connect(
            None, "erc721transfer", controller="erc721_transfer", action="execute"
        )
        self._route_map.connect(
            None, "erc20transfer", controller="erc20_transfer", action="execute"
        )

    def set_rollup_address(self, rollup_address):
        self._controllers["erc721_withdraw"].rollup_address = rollup_address
        self._controllers["donation_end"].rollup_address = rollup_address

    def process(self, route, request=None):
        route = route.lower()
        match_result = self._route_map.match(route)
        if match_result is None:
            return Error(f"Operation '{route}' is not supported")
        else:
            controller = self._controllers.get(match_result["controller"])
            logger.info(f"Executing operation '{route}'")
            return controller.execute(match_result, request)
