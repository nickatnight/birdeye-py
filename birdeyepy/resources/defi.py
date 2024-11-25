from typing import Optional, cast

from birdeyepy.utils import (
    DEFAULT_SOL_ADDRESS,
    BirdEyeApiUrls,
    BirdEyeRequestParams,
    IHttp,
    as_api_args,
)


class DeFi:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    @as_api_args
    def price(
        self,
        *,
        address: Optional[str] = DEFAULT_SOL_ADDRESS,
        check_liquidity: Optional[int] = 100,
        include_liquidity: Optional[bool] = None,
    ) -> list:
        """Get price update of a token.

        :param address:             The address of the token.
        :param check_liquidity:     The minimum liquidity to check.
        :param include_liquidity:   Include liquidity in the response.
        """
        params = {"address": address, "check_liquidity": check_liquidity}

        if include_liquidity is not None:
            params["include_liquidity"] = include_liquidity

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(path=BirdEyeApiUrls.DEFI_PRICE, **request)

        return cast(list, response)

    def history(
        self,
        *,
        time_from: int,
        time_to: int,
        address: Optional[str] = DEFAULT_SOL_ADDRESS,
        address_type: Optional[str] = "token",
        type_in_time: Optional[str] = "15m",
    ) -> dict:
        """Get historical price line chart of a token.

        :param time_from:       Specify the start time using Unix timestamps in seconds
        :param time_to:         Specify the end time using Unix timestamps in seconds
        :param address:         The address of the token.
        :param address_type:    The type of the address...defaults to 'token'
        :param type_in_time:    The type of time...defaults to '15m'
        """
        params = {
            "address": address,
            "address_type": address_type,
            "type": type_in_time,
            "time_from": time_from,
            "time_to": time_to,
        }

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(path=BirdEyeApiUrls.DEFI_HISTORY_PRICE, **request)

        return cast(dict, response)

    def supported_networks(self) -> dict:
        """Get a list of all supported networks."""
        response = self.http.send(path=BirdEyeApiUrls.DEFI_SUPPORTED_NETWORKS)

        return cast(dict, response)

    @as_api_args
    def price_multiple(
        self,
        *,
        addresses: list | str,
        check_liquidity: Optional[int] = 100,
        include_liquidity: Optional[bool] = None,
    ) -> dict:
        """Get price updates of multiple tokens in a single API call. Maximum 100 tokens

        :param addresses:           The addresses of the tokens.
        :param check_liquidity:     The minimum liquidity to check.
        :param include_liquidity:   Include liquidity in the response.
        """
        params = {"list_address": addresses, "check_liquidity": check_liquidity}

        if include_liquidity is not None:
            params["include_liquidity"] = include_liquidity

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(path=BirdEyeApiUrls.DEFI_PRICE_MULTIPLE, **request)

        return cast(dict, response)

    def history_by_unix(self, *, address: str, unixtime: int) -> dict:
        """Get historical price of a token at a specific Unix time.

        :param address:     The address of the token.
        :param unixtime:    The Unix time.
        """
        params = {"address": address, "time": unixtime}

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(
            path=BirdEyeApiUrls.DEFI_HISTORY_PRICE_BY_UNIX, **request
        )

        return cast(dict, response)

    def trades_token(
        self,
        *,
        address: Optional[str] = DEFAULT_SOL_ADDRESS,
        tx_type: Optional[str] = "swap",
        sort_type: Optional[str] = "desc",
        offset: Optional[int] = 0,
        limit: Optional[int] = 50,
    ) -> dict:
        """Get trades of a token.

        :param address:     The address of the token.
        :param tx_type:     The type of transaction.
        :param sort_type:   The type of sorting.
        :param limit:       The limit.
        """
        params = {
            "address": address,
            "tx_type": tx_type,
            "sort_type": sort_type,
            "offset": offset,
            "limit": limit,
        }

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(path=BirdEyeApiUrls.DEFI_TRADES_TOKEN, **request)

        return cast(dict, response)

    def trades_pair(
        self,
        *,
        address: str,
        tx_type: Optional[str] = "swap",
        sort_type: Optional[str] = "desc",
        offset: Optional[int] = 0,
        limit: Optional[int] = 50,
    ) -> dict:
        """Get list of trades of a certain pair or market.

        :param address:     The address of the token.
        :param tx_type:     The type of transaction.
        :param sort_type:   The type of sorting.
        :param limit:       The limit.
        """
        params = {
            "address": address,
            "tx_type": tx_type,
            "sort_type": sort_type,
            "offset": offset,
            "limit": limit,
        }

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(path=BirdEyeApiUrls.DEFI_TRADES_PAIR, **request)

        return cast(dict, response)

    def trades_token_by_time(
        self,
        *,
        address: Optional[str] = DEFAULT_SOL_ADDRESS,
        tx_type: Optional[str] = "swap",
        sort_type: Optional[str] = "desc",
        offset: Optional[int] = 0,
        limit: Optional[int] = 50,
        before_time: Optional[int] = 0,
        after_time: Optional[int] = 0,
    ) -> dict:
        """Get list of trades of a token with time bound option."""
        params = {
            "address": address,
            "tx_type": tx_type,
            "sort_type": sort_type,
            "offset": offset,
            "limit": limit,
            "before_time": before_time,
            "after_time": after_time,
        }

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(
            path=BirdEyeApiUrls.DEFI_TRADES_TOKEN_BY_TIME, **request
        )

        return cast(dict, response)

    def trades_pair_by_time(
        self,
        *,
        address: Optional[str] = DEFAULT_SOL_ADDRESS,
        tx_type: Optional[str] = "swap",
        sort_type: Optional[str] = "desc",
        offset: Optional[int] = 0,
        limit: Optional[int] = 50,
        before_time: Optional[int] = 0,
        after_time: Optional[int] = 0,
    ) -> dict:
        """Get list of trades of a certain pair or market with time bound option."""
        params = {
            "address": address,
            "tx_type": tx_type,
            "sort_type": sort_type,
            "offset": offset,
            "limit": limit,
            "before_time": before_time,
            "after_time": after_time,
        }

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(
            path=BirdEyeApiUrls.DEFI_TRADES_PAIR_BY_TIME, **request
        )

        return cast(dict, response)

    def ohlcv(
        self,
        *,
        address: str,
        time_from: int,
        time_to: int,
        type_in_time: Optional[str] = "15m",
    ) -> dict:
        """Get OHLCV price of a token.

        :param address:         The address of the token.
        :param time_from:       Specify the start time using Unix timestamps in seconds
        :param time_to:         Specify the end time using Unix timestamps in seconds
        :param type_in_time:    The type of time...defaults to '15m'
        """
        params = {
            "address": address,
            "time_from": time_from,
            "time_to": time_to,
            "type": type_in_time,
        }

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(path=BirdEyeApiUrls.DEFI_OHLCV, **request)

        return cast(dict, response)

    def ohlcv_pair(
        self,
        *,
        address: str,
        time_from: int,
        time_to: int,
        type_in_time: Optional[str] = "15m",
    ) -> dict:
        """Get OHLCV price of a pair.

        :param address:         The address of the token.
        :param time_from:       Specify the start time using Unix timestamps in seconds
        :param time_to:         Specify the end time using Unix timestamps in seconds
        :param type_in_time:    The type of time...defaults to '15m'
        """
        params = {
            "address": address,
            "time_from": time_from,
            "time_to": time_to,
            "type": type_in_time,
        }

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(path=BirdEyeApiUrls.DEFI_OHLCV_PAIR, **request)

        return cast(dict, response)

    def volume_price_single(
        self, *, address: str, type_in_time: Optional[str] = "24h"
    ) -> dict:
        """Get volume and price of a token.

        :param address:         The address of the token.
        :param type_in_time:    The type of time...defaults to '24h'
        """
        params = {"address": address, "type": type_in_time}

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(path=BirdEyeApiUrls.DEFI_VOLUME_SINGLE, **request)

        return cast(dict, response)
