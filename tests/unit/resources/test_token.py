from unittest.mock import MagicMock

import pytest

from birdeyepy.resources.token import Token
from birdeyepy.utils import BirdEyeApiUrls


def test_token_list_all_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Token(http=mock_http)
    client.list_all()

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.DEFI_TOKEN_LIST,
        params={
            "sort_by": "v24hUSD",
            "sort_type": "desc",
            "offset": 0,
            "limit": 50,
            "min_liquidity": 50,
        },
    )


def test_token_security_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Token(http=mock_http)
    client.security(address="test")

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.TOKEN_SECURITY,
        params={"address": "test"},
    )


def test_token_overview_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Token(http=mock_http)
    client.overview(address="test")

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.TOKEN_OVERVIEW,
        params={"address": "test"},
    )


def test_token_creation_info_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Token(http=mock_http)
    client.creation_info(address="test")

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.TOKEN_CREATION_INFO,
        params={"address": "test"},
    )


def test_token_trending_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Token(http=mock_http)
    client.trending()

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.TOKEN_TRENDING,
        params={
            "sort_by": "rank",
            "sort_type": "asc",
            "offset": 0,
            "limit": 10,
        },
    )


def test_token_list_all_v2_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Token(http=mock_http)
    client.list_all_v2()

    # Assert
    mock_http.send.assert_called_once_with(
        method="POST",
        path=BirdEyeApiUrls.TOKEN_LIST_V2,
    )


def test_token_new_listing_api_called_with_expected_args_default() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Token(http=mock_http)
    client.new_listing(time_to=1732472285)

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.TOKEN_NEW_LISTING,
        params={"time_to": 1732472285},
    )


def test_token_new_listing_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Token(http=mock_http)
    client.new_listing(time_to=1732472285, limit=10, meme_platform_enabled=True)

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.TOKEN_NEW_LISTING,
        params={"time_to": 1732472285, "limit": 10, "meme_platform_enabled": "true"},
    )


def test_token_top_traders_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Token(http=mock_http)
    client.top_traders(address="test")

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.TOKEN_TOP_TRADERS,
        params={
            "address": "test",
            "time_frame": "24h",
            "sort_type": "desc",
            "sort_by": "volume",
            "offset": 0,
            "limit": 10,
        },
    )


def test_token_all_markets_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Token(http=mock_http)
    client.all_markets(address="test")

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.TOKEN_ALL_MARKETS,
        params={
            "address": "test",
            "time_frame": "24h",
            "sort_type": "desc",
            "sort_by": "liquidity",
            "offset": 0,
            "limit": 10,
        },
    )


def test_token_market_metadata_single_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Token(http=mock_http)
    client.market_metadata_single(address="test")

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.TOKEN_METADATA_SINGLE,
        params={"address": "test"},
    )


@pytest.mark.parametrize(
    "addresses,expected_params",
    [
        ("test", {"list_address": "test"}),
        (["test1", "test2"], {"list_address": "test1,test2"}),
        ("test1,test2", {"list_address": "test1,test2"}),
    ],
)
def test_token_market_metadata_multiple_api_called_with_expected_args(
    addresses: str | list[str], expected_params: dict
) -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Token(http=mock_http)
    client.market_metadata_multiple(addresses=addresses)

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.TOKEN_METADATA_MULTIPLE,
        params=expected_params,
    )


def test_token_market_data_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Token(http=mock_http)
    client.market_data(address="test")

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.TOKEN_MARKET_DATA,
        params={"address": "test"},
    )


def test_token_trade_data_single_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Token(http=mock_http)
    client.trade_data_single(address="test")

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.TOKEN_TRADE_DATA_SINGLE,
        params={"address": "test"},
    )


@pytest.mark.parametrize(
    "addresses,expected_params",
    [
        ("test", {"list_address": "test"}),
        (["test1", "test2"], {"list_address": "test1,test2"}),
        ("test1,test2", {"list_address": "test1,test2"}),
    ],
)
def test_token_trade_data_multiple_api_called_with_expected_args(
    addresses: str | list[str], expected_params: dict
) -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Token(http=mock_http)
    client.trade_data_multiple(addresses=addresses)

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.TOKEN_TRADE_DATA_MULTIPLE,
        params=expected_params,
    )


def test_token_holder_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Token(http=mock_http)
    client.holder(address="test")

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.TOKEN_HOLDER,
        params={"address": "test", "offset": 0, "limit": 100},
    )
