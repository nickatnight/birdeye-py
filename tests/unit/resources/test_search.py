# mypy: disable-error-code="attr-defined"
from unittest.mock import MagicMock

from birdeyepy.birdeye import BirdEye
from birdeyepy.resources.search import Search
from birdeyepy.utils import BirdEyeApiUrls


def test_search_token_market_data_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Search(http=mock_http)
    client.token_market_data(
        keyword="test",
        verify_token=True,
        markets=["test"],
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.SEARCH_TOKEN_MARKET_DATA,
        params={
            "offset": 0,
            "limit": 20,
            "chain": "all",
            "keyword": "test",
            "sort_by": "volume_24h_usd",
            "sort_type": "desc",
            "verify_token": "true",
            "markets": "test",
        },
    )


def test_search_token_market_data_removes_header(mocker: MagicMock) -> None:
    # Arrange
    client = BirdEye(api_key="test")
    mocker.patch.object(client.search.http, "send")

    # Act
    client.search.token_market_data(
        keyword="test",
        verify_token=True,
        markets=["test"],
    )

    # Assert
    assert "x-chain" in client.search.http.s.headers
    assert client.search.http.s.headers["x-chain"] == "solana"
