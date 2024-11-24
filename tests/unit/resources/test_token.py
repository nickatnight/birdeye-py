from unittest.mock import MagicMock

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
