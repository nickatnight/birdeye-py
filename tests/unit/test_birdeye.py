from unittest.mock import MagicMock

from birdeyepy.birdeye import BirdEye, __version__
from birdeyepy.resources import RESOURCE_MAP
from birdeyepy.utils import BASE_BIRD_EYE_API_URL


def test_client_http_called_with_correct_args(mocker: MagicMock) -> None:
    # Arrange
    mock_requests_client = mocker.patch("birdeyepy.birdeye.RequestsClient")

    # Act
    _ = BirdEye(api_key="test")

    # Assert
    mock_requests_client.assert_called_once_with(
        base_url=BASE_BIRD_EYE_API_URL,
        headers={"X-API-KEY": "test", "User-Agent": f"birdeyepy/v{__version__}"},
    )


def test_client_properties(
    mocker: MagicMock,
) -> None:
    # Arrange
    mocker.patch("birdeyepy.birdeye.RequestsClient")

    # Act
    client = BirdEye(api_key="test")

    # Assert
    for resource_name, _ in RESOURCE_MAP.items():
        assert hasattr(client, resource_name)
