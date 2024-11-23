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
