from unittest.mock import MagicMock

from birdeyepy.resources.wallet import Wallet
from birdeyepy.utils import BirdEyeApiUrls


def test_wallet_supported_networks_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Wallet(http=mock_http)
    client.supported_networks()

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.WALLET_SUPPORTED_NETWORKS
    )


def test_wallet_portfolio_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Wallet(http=mock_http)
    client.portfolio(wallet="test")

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.WALLET_PORTFOLIO,
        params={"wallet": "test"},
    )


def test_wallet_portfolio_multichain_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Wallet(http=mock_http)
    client.portfolio_multichain(wallet="test")

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.WALLET_PORTFOLIO_MULTICHAIN,
        params={"wallet": "test"},
    )


def test_wallet_token_balance_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Wallet(http=mock_http)
    client.token_balance(wallet="test", token_address="test")

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.WALLET_TOKEN_BALANCE,
        params={"wallet": "test", "address": "test"},
    )


def test_wallet_transaction_history_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Wallet(http=mock_http)
    client.transaction_history(wallet="test")

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.WALLET_TRANSACTION_HISTORY,
        params={"wallet": "test", "limit": 100},
    )


def test_wallet_transaction_history_multichain_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Wallet(http=mock_http)
    client.transaction_history_multichain(wallet="test")

    # Assert
    mock_http.send.assert_called_once_with(
        path=BirdEyeApiUrls.WALLET_TRANSACTION_HISTORY_MULTICHAIN,
        params={"wallet": "test"},
    )


def test_wallet_transaction_simulation_api_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()

    # Act
    client = Wallet(http=mock_http)
    client.transaction_simulation(
        from_address="test", to_address="test", value="test", data="test"
    )

    # Assert
    mock_http.send.assert_called_once_with(
        method="POST",
        path=BirdEyeApiUrls.WALLET_TRANSACTION_SIMULATION,
        params={"from": "test", "to": "test", "value": "test", "data": "test"},
    )
