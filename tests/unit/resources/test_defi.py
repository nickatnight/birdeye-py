from unittest.mock import MagicMock

from birdeyepy.resources.defi import DeFi
from birdeyepy.utils import DEFAULT_SOL_ADDRESS, BirdEyeApiUrls


def test_defi_price_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = DeFi(http=mock_http)
    client.price(address="test", include_liquidity=True)

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.DEFI_PRICE,
        params={"address": "test", "check_liquidity": 100, "include_liquidity": "true"},
    )


def test_defi_history_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = DeFi(http=mock_http)
    client.history(
        time_from=1,
        time_to=2,
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.DEFI_HISTORY_PRICE,
        params={
            "time_from": 1,
            "time_to": 2,
            "address": DEFAULT_SOL_ADDRESS,
            "address_type": "token",
            "type": "15m",
        },
    )
