from unittest.mock import MagicMock

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
