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


def test_defi_supported_networks_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = DeFi(http=mock_http)
    client.supported_networks()

    # Assert
    mock_http.send.assert_called_once_with(path=BirdEyeApiUrls.DEFI_SUPPORTED_NETWORKS)


def test_defi_price_multiple_args_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = DeFi(http=mock_http)
    client.price_multiple(addresses="test", check_liquidity=50, include_liquidity=False)

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.DEFI_PRICE_MULTIPLE,
        params={
            "list_address": "test",
            "check_liquidity": 50,
            "include_liquidity": "false",
        },
    )


def test_defi_history_by_unix_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = DeFi(http=mock_http)
    client.history_by_unix(address="test", unixtime=1)

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.DEFI_HISTORY_PRICE_BY_UNIX,
        params={"address": "test", "time": 1},
    )


def test_defi_trades_token_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = DeFi(http=mock_http)
    client.trades_token(address="test")

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.DEFI_TRADES_TOKEN,
        params={
            "address": "test",
            "tx_type": "swap",
            "sort_type": "desc",
            "offset": 0,
            "limit": 50,
        },
    )


def test_defi_trades_pair_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = DeFi(http=mock_http)
    client.trades_pair(address="test")

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.DEFI_TRADES_PAIR,
        params={
            "address": "test",
            "tx_type": "swap",
            "sort_type": "desc",
            "offset": 0,
            "limit": 50,
        },
    )


def test_defi_trades_token_by_time_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = DeFi(http=mock_http)
    client.trades_token_by_time(
        address="test",
        before_time=1,
        after_time=2,
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.DEFI_TRADES_TOKEN_BY_TIME,
        params={
            "address": "test",
            "before_time": 1,
            "after_time": 2,
            "tx_type": "swap",
            "sort_type": "desc",
            "offset": 0,
            "limit": 50,
        },
    )


def test_defi_trades_pair_by_time_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = DeFi(http=mock_http)
    client.trades_pair_by_time(
        address="test",
        before_time=1,
        after_time=2,
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.DEFI_TRADES_PAIR_BY_TIME,
        params={
            "address": "test",
            "before_time": 1,
            "after_time": 2,
            "tx_type": "swap",
            "sort_type": "desc",
            "offset": 0,
            "limit": 50,
        },
    )


def test_defi_ohlcv_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = DeFi(http=mock_http)
    client.ohlcv(
        address="test",
        time_from=1,
        time_to=2,
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.DEFI_OHLCV,
        params={
            "address": "test",
            "time_from": 1,
            "time_to": 2,
            "type": "15m",
        },
    )


def test_defi_ohlcv_pair_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = DeFi(http=mock_http)
    client.ohlcv_pair(
        address="test",
        time_from=1,
        time_to=2,
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.DEFI_OHLCV_PAIR,
        params={
            "address": "test",
            "time_from": 1,
            "time_to": 2,
            "type": "15m",
        },
    )


def test_defi_volume_price_single_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = DeFi(http=mock_http)
    client.volume_price_single(address="test")

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.DEFI_VOLUME_SINGLE,
        params={"address": "test", "type": "24h"},
    )
