from birdeyepy.resources import RESOURCE_MAP
from birdeyepy.utils import (
    BASE_BIRD_EYE_API_URL,
    BirdEyeChain,
    BirdEyeClientError,
    RequestsClient,
)


__version__ = "0.0.2"


class BirdEye:
    """API Client for BirdEye"""

    def __init__(self, api_key: str, chain: str = BirdEyeChain.SOLANA) -> None:
        if chain not in BirdEyeChain.all():
            raise BirdEyeClientError(f"Invalid chain: {chain}")

        _http = RequestsClient(
            base_url=BASE_BIRD_EYE_API_URL,
            headers={
                "x-chain": chain,
                "X-API-KEY": api_key,
                "User-Agent": f"birdeyepy/v{__version__}",
            },
        )

        for resource_name, resource_class in RESOURCE_MAP.items():
            setattr(self, resource_name, resource_class(http=_http))
