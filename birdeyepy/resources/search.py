from typing import Optional, cast

from birdeyepy.utils import BirdEyeApiUrls, BirdEyeRequestParams, IHttp, as_api_args


class Search:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    @as_api_args
    def token_market_data(
        self,
        *,
        keyword: str,
        markets: list[str] | str,
        sort_by: Optional[str] = "volume_24h_usd",
        sort_type: Optional[str] = "desc",
        verify_token: Optional[bool] = None,
        chain: Optional[str] = "all",
        offset: Optional[int] = 0,
        limit: Optional[int] = 20,
    ) -> dict:
        """Search for token and market data by matching a pattern or a specific token, market address.

        :param list_address:        A list of addresses
        """
        params = {
            "offset": offset,
            "limit": limit,
            "chain": chain,
            "keyword": keyword,
            "sort_by": sort_by,
            "sort_type": sort_type,
            "verify_token": verify_token,
            "markets": markets,
        }

        if verify_token is not None:
            params["verify_token"] = verify_token

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(
            path=BirdEyeApiUrls.SEARCH_TOKEN_MARKET_DATA, **request
        )

        return cast(dict, response)
