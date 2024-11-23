from birdeyepy.resources import RESOURCE_MAP
from birdeyepy.utils import BASE_BIRD_EYE_API_URL, RequestsClient


__version__ = "0.0.1"


class BirdEye:
    """API Client for BirdEye"""

    def __init__(self, api_key: str) -> None:
        _http = RequestsClient(
            base_url=BASE_BIRD_EYE_API_URL,
            headers={"X-API-KEY": api_key, "User-Agent": f"birdeyepy/v{__version__}"},
        )

        for resource_name, resource_class in RESOURCE_MAP.items():
            setattr(self, resource_name, resource_class(http=_http))
