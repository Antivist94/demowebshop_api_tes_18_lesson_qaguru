import json
import logging

import allure
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType


def add_to_cart(url, **kwargs):
    with step("API_Положить товар в корзину и передать куки сессии пользователя"):
        response = requests.post(url, kwargs)
        allure.attach(body = json.dumps(response.json(), indent = 4, ensure_ascii = True), name = "Response",
                      attachment_type = AttachmentType.JSON, extension = "json")
        logging.info(response.request.url)
        logging.info(response.status_code)
        logging.info(response.text)
    return response
