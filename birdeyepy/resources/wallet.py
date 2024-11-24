from typing import Optional, cast

from birdeyepy.utils import BirdEyeApiUrls, BirdEyeRequestParams, IHttp


class Wallet:
    """The api is still in beta and may change in the future."""

    def __init__(self, http: IHttp) -> None:
        self.http = http

    def supported_networks(self) -> dict:
        """Get supported networks."""
        response = self.http.send(path=BirdEyeApiUrls.WALLET_SUPPORTED_NETWORKS)

        return cast(dict, response)

    def portfolio(self, wallet: str) -> dict:
        """Get portfolio of a wallet.

        :param address:     The address of the wallet.
        """
        params = {"wallet": wallet}

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(path=BirdEyeApiUrls.WALLET_PORTFOLIO, **request)

        return cast(dict, response)

    def portfolio_multichain(self, wallet: str) -> dict:
        """Get portfolio of a wallet across multiple chains.

        :param address:     The address of the wallet.
        """
        params = {"wallet": wallet}

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(
            path=BirdEyeApiUrls.WALLET_PORTFOLIO_MULTICHAIN, **request
        )

        return cast(dict, response)

    def token_balance(self, wallet: str, token_address: str) -> dict:
        """Get token balance of a wallet.

        :param wallet:          The address of the wallet.
        :param token_address:   The address of the token.
        """
        params = {"wallet": wallet, "address": token_address}

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(path=BirdEyeApiUrls.WALLET_TOKEN_BALANCE, **request)

        return cast(dict, response)

    def transaction_history(
        self, wallet: str, limit: Optional[int] = 100, before: Optional[str] = None
    ) -> dict:
        """Get transaction history of a wallet.

        :param wallet:      The address of the wallet.
        :param limit:       The number of results to return.
        :param before:      A transaction hash to traverse starting from. Only works with Solana
        """
        params = {"wallet": wallet, "limit": limit}

        if before is not None:
            params["before"] = before

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(
            path=BirdEyeApiUrls.WALLET_TRANSACTION_HISTORY, **request
        )

        return cast(dict, response)

    def transaction_history_multichain(self, wallet: str) -> dict:
        """Get transaction history of a wallet across multiple chains.

        :param wallet:      The address of the wallet.
        """
        params = {"wallet": wallet}

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(
            path=BirdEyeApiUrls.WALLET_TRANSACTION_HISTORY_MULTICHAIN, **request
        )

        return cast(dict, response)

    def transaction_simulation(
        self, from_address: str, to_address: str, value: str, data: str
    ) -> dict:
        """Simulate a transaction.

        :param from_address:    The address of the sender.
        :param to_address:      The address of the receiver.
        :param value:           The value to send.
        :param data:            The data to send.
        """
        params = {"from": from_address, "to": to_address, "value": value, "data": data}

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(
            method="POST", path=BirdEyeApiUrls.WALLET_TRANSACTION_SIMULATION, **request
        )

        return cast(dict, response)
