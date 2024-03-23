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

import itertools
from datetime import datetime


class DisasterReport:
    """
    Disaster to donate to
    """

    def __init__(self, erc721: str, token_id: int):
        self._erc721 = erc721
        self._token_id = token_id

    @property
    def erc721(self):
        return self._erc721

    @property
    def token_id(self):
        return self._token_id

    def __eq__(self, other):
        return self.erc721 == other.erc721 and self.token_id == other.token_id

    def __ne__(self, other):
        return self.erc721 != other.erc721 or self.token_id != other.token_id


class Amount:
    """
    Amount to donate

    Identifies the `amount` placed by a donator to support disaster alleviation
    """

    def __init__(self, donation_id: int, donator: str, amount: int, timestamp: datetime):
        if amount <= 0:
            raise ValueError(f"Amount ({amount}) must be greater than zero")

        self._donation_id = donation_id
        self._donator = donator
        self._amount = amount
        self._timestamp = timestamp

    @property
    def post_id(self):
        return self._post_id

    @property
    def donator(self):
        return self._donator

    @property
    def amount(self):
        return self._amount

    @property
    def timestamp(self):
        return self._timestamp

    def __eq__(self, other):
        return (
            self.donator == other.donator
            and self.post_id == other.post_id
            and self.amount == other.amount
            and self.timestamp == other.timestamp
        )

    def __ne__(self, other):
        return not (self == other)

    def __gt__(self, other):
        return self.amount > other.amount or (
            self.amount == other.amount and self.timestamp < other.timestamp
        )

    def __lt__(self, other):
        return self.amount < other.amount or (
            self.amount == other.amount and self.timestamp > other.timestamp
        )

    def __ge__(self, other):
        return NotImplemented

    def __le__(self, other):
        return NotImplemented


class Donation:
    """
    Donation

    It has a `title` and `description`,
    and may be in three different states: `CREATED`,` STARTED` or `FINISHED`.
    """

    CREATED = 0
    STARTED = 1
    FINISHED = 2

    _id = itertools.count()

    def __init__(
        self,
        creator: str,
        disaster_report: DisasterReport,
        erc20: str,
        title: str,
        description: str,
        start_date: datetime,
        end_date: datetime,
    ):
        if end_date <= start_date:
            raise ValueError(
                f"End date ({end_date}) must be after start date ({start_date})"
            )

        self._id = next(self._id)
        self._state = Donation.CREATED
        self._creator = creator
        self._disaster_report = disaster_report
        self._erc20 = erc20
        self._title = title
        self._description = description
        self._start_date = start_date
        self._end_date = end_date

    @property
    def id(self):
        return self._id

    @property
    def state(self):
        return self._state

    @property
    def creator(self):
        return self._creator

    @property
    def item(self):
        return self._item

    @property
    def erc20(self):
        return self._erc20

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def start_date(self):
        return self._start_date

    @property
    def end_date(self):
        return self._end_date


    def __lt__(self, other):
        return self.id < other.id

    def donate(self, amount: Amount):
        if self.state == Donation.FINISHED:
            raise ValueError("The donation has ended, look for other disasters to donate to")

        if amount.donation_id != self.id:
            raise ValueError(f"Donation id ({amount.donation_id}) does not match")



        if self.state == Donation.CREATED:
            self._state = Donation.STARTED

    def finish(self):
        self._state = Donation.FINISHED
