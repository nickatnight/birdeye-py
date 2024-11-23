from typing import Optional, cast

from birdeyepy.utils import BirdEyeApiUrls, BirdEyeRequestParams, IHttp


class Token:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def list_all(
        self,
        *,
        sort_by: Optional[str] = "v24hUSD",
        sort_type: Optional[str] = "desc",
        offset: Optional[int] = 0,
        limit: Optional[int] = 50,
        min_liquidity: Optional[int] = 50,
    ) -> list:
        """Get token list of any supported chains.

        :param sort_by:         The field to sort by.
        :param sort_type:       The type of sorting.
        :param offset:          The offset
        :param limit:           The limit
        :param min_liquidity:   The minimum liquidity to check.
        """
        params = {
            "sort_by": sort_by,
            "sort_type": sort_type,
            "offset": offset,
            "limit": limit,
            "min_liquidity": min_liquidity,
        }

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(path=BirdEyeApiUrls.DEFI_TOKEN_LIST, **request)

        return cast(list, response)
