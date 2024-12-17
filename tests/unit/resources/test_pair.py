from unittest.mock import MagicMock

from birdeyepy.resources.pair import Pair
from birdeyepy.utils import BirdEyeApiUrls


def test_pair_overview_multiple_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Pair(http=mock_http)
    client.overview_multiple(list_address=["test1", "test2"])

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.PAIR_OVERVIEW_MULTIPLE,
        params={"list_address": "test1,test2"},
    )


def test_pair_overview_single_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Pair(http=mock_http)
    client.overview_single(address="test1")

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.PAIR_OVERVIEW_SINGLE,
        params={"address": "test1"},
    )
