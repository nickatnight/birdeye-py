from unittest.mock import MagicMock

from birdeyepy.resources.trader import Trader
from birdeyepy.utils import BirdEyeApiUrls


def test_trader_gainers_losers_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Trader(http=mock_http)
    client.gainers_losers()

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.TRADER_GAINERS_LOSERS,
        params={
            "time_frame": "1W",
            "sort_by": "PnL",
            "sort_type": "desc",
            "offset": 0,
            "limit": 10,
        },
    )


def test_trader_seek_by_time_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Trader(http=mock_http)
    client.seek_by_time(address="test")

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.TRADER_SEEK_BY_TIME,
        params={
            "address": "test",
            "tx_type": "swap",
            "sort_type": "desc",
            "offset": 0,
            "limit": 100,
            "before_time": 0,
            "after_time": 0,
        },
    )
