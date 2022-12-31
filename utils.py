from io import BytesIO
from typing import Union

import requests


def make_image(url: str) -> Union[bytes, str]:
    response = requests.get(url)
    return BytesIO(response.content).read()
