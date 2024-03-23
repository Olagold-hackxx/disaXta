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
from operator import attrgetter

import donation.wallet as Wallet
from donation.encoders import DonationEncoder, AmountEncoder
from donation.log import logger
from donation.model import Donation, DisasterReport
from donation.outputs import Error, Log, Notice, Output


class Donatee:

    def __init__(self, wallet: Wallet):
        self._donations: dict[int, DisasterReport] = {}
        self._wallet = wallet

    def donation_create(
        self,
        donatee: str,
        disaster_report: DisasterReport,
        erc20: str,
        title: str,
        description: str,
        amount: int,
        start_date: datetime,
        end_date: datetime,
        current_date: datetime,
    ):

        try:
            donation = Donation(
                donatee,
                disaster_report,
                erc20,
                title,
                description,
                start_date,
                end_date,
                amount,
            )
            self._donations[donation._id] = donation

            donation_json = json.dumps(donation, cls=DonationEncoder)
            notice_payload = f'{{"type": "donation_create", "content": {donation_json}}}'
            logger.info(
                f"Donation {donation._id} created for a disaster "
                f"'ERC-721: {disaster_report.erc721}, id: {disaster_report.token_id}'"
            )
            return Notice(notice_payload)
        except Exception as error:
            error_msg = f"Failed to create donation. {error}"
            logger.debug(error_msg, exc_info=True)
            return Error(error_msg)

    def _has_enough_funds(self, erc20, donator, amount):
        balance = self._wallet.balance_get(donator)
        erc20_balance = balance.erc20_get(erc20)

        return amount <= erc20_balance
