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
import web3
import base64
import logging
import requests
import traceback
from enum import Enum
from os import environ
from io import BytesIO
from analysis_model import prediction
from recognition_model import recognition

logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

rollup_server = environ["ROLLUP_HTTP_SERVER_URL"]
logger.info(f"HTTP rollup_server url is {rollup_server}")

NETWORK = environ["NETWORK"]
logger.info(f"NETWORK is {NETWORK}")

networks = json.load(open("networks.json"))


def str2hex(string):
    """
    Encode a string as an hex string
    """
    return binary2hex(str2binary(string))


def str2binary(string):
    """
    Encode a string as an binary string
    """
    return string.encode("utf-8")


def binary2hex(binary):
    """
    Encode a binary as an hex string
    """
    return "0x" + binary.hex()


def hex2binary(hexstr):
    """
    Decodes a hex string into a regular byte string
    """
    return bytes.fromhex(hexstr[2:])


def hex2str(hexstr):
    """
    Decodes a hex string into a regular string
    """
    return hex2binary(hexstr).decode("utf-8")


def send_notice(notice: str) -> None:
    send_post("notice", notice)


def send_voucher(voucher: str) -> None:
    send_post("voucher", voucher)


def send_report(report: str) -> None:
    send_post("report", report)


def send_post(endpoint, json_data) -> None:
    response = requests.post(rollup_server + f"/{endpoint}", json=json_data)
    logger.info(
        f"/{endpoint}: Received response status {response.status_code} body {response.content}")



def analysis_model_inference(data):
    location = data['location']
    start_date = data['startDate']
    end_date = data['endDate']
    disaster_type = data['disasterType']
    key = data["apiKey"]
    return json.dumps(prediction.predict(location, start_date, end_date, disaster_type, key))

def recognition_model_inferencedat(data):
    image_file = data["base64_image"]
    if image_file:
        recognition_response = recognition.process_image(image_file=image_file)
        return json.dumps({"status": 200, "data": recognition_response, "ok": True})
    else:
        return json.dumps({"status": 400, "error": "Bad request", "message": "Base64 image must be provided", "ok": False})


def handle_advance(data):
    logger.info(f"Received advance request data {data}.")
    logger.info(f"Current network is {NETWORK}")

    try:
        voucher = None
        payload = data["payload"]
        binary = hex2binary(payload)
        sender = data["metadata"]["msg_sender"]

        if sender == FOREST_RESERVE_ADDRESS:
            if verify_real_world_state(binary):
                voucher = create_verifier_voucher(
                    INCREASE_ALLOWANCE_FUNCTION_SELECTOR, FOREST_RESERVE_ADDRESS)
            else:
                send_report({"payload": str2hex(
                    f"Invalid real world state {binary}")})
        else:
            logger.info(
                f"sender {sender} is not fores reserve address {FOREST_RESERVE_ADDRESS}")
        if voucher:
            logger.info(f"voucher {voucher}")
            send_voucher(voucher)
        return "accept"
    except Exception as e:
        msg = f"Error {e} processing data {data}"
        logger.error(f"{msg}\n{traceback.format_exc()}")
        send_report({"payload": str2hex(msg)})
        return "reject"


def handle_inspect(data):
    global STATE
    logger.info(f"Received inspect request data {data}")
    data_decoded = hex2binary(data["payload"]).decode('utf-8')
    try:
        if data_decoded == "status":
            send_report({"payload": str2hex(STATE.name)})
            return "accept"
        else:
            raise Exception(
                f"Unknown payload {data['payload']}, send 'status' to get current state")

    except Exception as e:
        msg = f"Error {e} processing data {data}"
        logger.error(f"{msg}\n{traceback.format_exc()}")
        send_report({"payload": str2hex(msg)})
        return "reject"

handlers = {
    "advance_state": handle_advance,
    "inspect_state": handle_inspect,
}


finish = {"status": "accept"}

while True:
    logger.info("Sending finish")
    response = requests.post(rollup_server + "/finish", json=finish)
    logger.info(f"Received finish status {response.status_code}")
    if response.status_code == 202:
        logger.info("No pending rollup request, trying again")
    else:
        rollup_request = response.json()
        data = rollup_request["data"]
        handler = handlers[rollup_request["request_type"]]
        finish["status"] = handler(rollup_request["data"])
