from birdeyepy.resources import RESOURCE_MAP
from birdeyepy.utils import (
    BASE_BIRD_EYE_API_URL,
    BirdEyeChainEnum,
    BirdEyeClientError,
    RequestsClient,
)


__version__ = "0.0.5"


class BirdEye:
    """API Client for BirdEye

    :param api_key:         The API key for the BirdEye. See here https://docs.birdeye.so/docs/authentication-api-keys
    :param chain:           The chain to use. Defaults to 'solana'
    """

    def __init__(self, api_key: str, chain: str = BirdEyeChainEnum.SOLANA) -> None:
        if chain not in BirdEyeChainEnum.all():
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
