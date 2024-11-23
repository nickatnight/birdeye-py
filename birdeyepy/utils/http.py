import copy
import logging
from typing import Any, Optional

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from birdeyepy.utils.exceptions import BirdEyeRequestError
from birdeyepy.utils.interfaces import IHttp


logger = logging.getLogger(__name__)
default_headers = {"Content-Type": "application/json"}


def _get_retry() -> Retry:
    return Retry(
        total=3,
        backoff_factor=2,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["HEAD", "GET", "OPTIONS"],
    )


def _get_headers(headers: Optional[dict] = None) -> dict:
    _headers = copy.deepcopy(default_headers)

    if headers is not None:
        _headers.update(**headers)

    return _headers


def _get_session(headers: Optional[dict] = None) -> requests.Session:
    s = requests.Session()
    adapter = HTTPAdapter(max_retries=_get_retry())
    _headers = _get_headers(headers)

    s.mount("https://", adapter)
    s.mount("http://", adapter)

    s.headers.update(_headers)

    return s


class RequestsClient(IHttp):
    def __init__(
        self, base_url: Optional[str] = "", headers: Optional[dict] = None
    ) -> None:
        self.base_url = base_url
        self.s = _get_session(headers)

    def send(self, path: str, method: str = "get", **extra: Any) -> dict | list:
        url = f"{self.base_url}{path}"
        headers = extra.pop("headers", {})

        self.s.headers.update(headers)

        req_to_call = getattr(self.s, method.lower())

        try:
            response = req_to_call(url, **extra)
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}", exc_info=True)
            raise BirdEyeRequestError(
                message=str(http_err), response=http_err.response
            ) from None
        except Exception as err:
            logger.error(f"Other error occurred: {err}")
            raise

        return response.json()  # type: ignore
