from typing import Optional, cast

from birdeyepy.utils import BirdEyeApiUrls, BirdEyeRequestParams, IHttp, as_api_args


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
    ) -> dict:
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

        return cast(dict, response)

    def security(self, address: str) -> dict:
        """Get token security of any supported chains.

        :param address:     The address of the token.
        """
        params = {"address": address}

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(path=BirdEyeApiUrls.TOKEN_SECURITY, **request)

        return cast(dict, response)

    def overview(self, address: str) -> dict:
        """Get overview of a token.

        :param address:     The address of the token.
        """
        params = {"address": address}

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(path=BirdEyeApiUrls.TOKEN_OVERVIEW, **request)

        return cast(dict, response)

    def creation_info(self, address: str) -> dict:
        """Get creation info of a token.

        :param address:     The address of the token.
        """
        params = {"address": address}

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(path=BirdEyeApiUrls.TOKEN_CREATION_INFO, **request)

        return cast(dict, response)

    def trending(
        self,
        sort_by: str = "rank",
        sort_type: str = "asc",
        offset: int = 0,
        limit: int = 10,
    ) -> dict:
        """Retrieve a dynamic and up-to-date list of trending tokens based on specified sorting criteria.

        :param sort_by:     The field to sort by.
        :param sort_type:   The type of sorting.
        :param offset:      The offset.
        :param limit:       The limit.
        """
        params = {
            "sort_by": sort_by,
            "sort_type": sort_type,
            "offset": offset,
            "limit": limit,
        }

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(path=BirdEyeApiUrls.TOKEN_TRENDING, **request)

        return cast(dict, response)

    def list_all_v2(self) -> dict:
        """This endpoint facilitates the retrieval of a list of tokens on a specified blockchain network. This upgraded version is exclusive to business and enterprise packages. By simply including the header for the requested blockchain without any query parameters, business and enterprise users can get the full list of tokens on the specified blockchain in the URL returned in the response. This removes the need for the limit response of the previous version and reduces the workload of making multiple calls."""
        response = self.http.send(path=BirdEyeApiUrls.TOKEN_LIST_V2, method="POST")

        return cast(dict, response)

    @as_api_args
    def new_listing(
        self,
        time_to: int,
        limit: Optional[int] = None,
        meme_platform_enabled: Optional[bool] = None,
    ) -> dict:
        """Get newly listed tokens of any supported chains.

        :param time_to:                 Specify the end time using Unix timestamps in seconds
        :param limit:                   The limit
        :param meme_platform_enabled:   Enable to receive token new listing from meme platforms (eg: pump.fun). This filter only supports Solana
        """
        params = {
            "time_to": time_to,
        }

        if limit is not None:
            params["limit"] = limit

        if meme_platform_enabled is not None:
            params["meme_platform_enabled"] = meme_platform_enabled

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(path=BirdEyeApiUrls.TOKEN_NEW_LISTING, **request)

        return cast(dict, response)

    def top_traders(
        self,
        address: str,
        time_frame: Optional[str] = "24h",
        sort_type: Optional[str] = "desc",
        sort_by: Optional[str] = "volume",
        offset: Optional[int] = 0,
        limit: Optional[int] = 10,
    ) -> dict:
        """Get top traders of given token.

        :param address:     The address of the token.
        :param time_frame:  The time frame for the data (e.g., '24h', '7d').
        :param sort_type:   The type of sorting.
        :param sort_by:     The field to sort by.
        :param offset:      The offset.
        :param limit:       The limit.
        """
        params = {
            "address": address,
            "time_frame": time_frame,
            "sort_type": sort_type,
            "sort_by": sort_by,
            "offset": offset,
            "limit": limit,
        }

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(path=BirdEyeApiUrls.TOKEN_TOP_TRADERS, **request)

        return cast(dict, response)

    def all_markets(
        self,
        address: str,
        time_frame: Optional[str] = "24h",
        sort_type: Optional[str] = "desc",
        sort_by: Optional[str] = "liquidity",
        offset: Optional[int] = 0,
        limit: Optional[int] = 10,
    ) -> dict:
        """The API provides detailed information about the markets for a specific cryptocurrency token on a specified blockchain. Users can retrieve data for one or multiple markets related to a single token. This endpoint requires the specification of a token address and the blockchain to filter results. Additionally, it supports optional query parameters such as offset, limit, and required sorting by liquidity or sort type (ascending or descending) to refine the output.

        :param address:     The address of the token.
        :param time_frame:  The time frame for the data (e.g., '24h', '7d').
        :param sort_type:   The type of sorting.
        :param sort_by:     The field to sort by.
        :param offset:      The offset.
        :param limit:       The limit.
        """
        params = {
            "address": address,
            "time_frame": time_frame,
            "sort_type": sort_type,
            "sort_by": sort_by,
            "offset": offset,
            "limit": limit,
        }

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(path=BirdEyeApiUrls.TOKEN_ALL_MARKETS, **request)

        return cast(dict, response)

    def market_metadata_single(self, address: str) -> dict:
        """Get metadata of single token

        :param address:       The address of the token.
        """
        params = {"address": address}

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(path=BirdEyeApiUrls.TOKEN_METADATA_SINGLE, **request)

        return cast(dict, response)

    @as_api_args
    def market_metadata_multiple(self, addresses: str | list[str]) -> dict:
        """Get metadata of multiple tokens

        :param addresses:       The address of the token...can be comma separated string or list of strings.
        """
        params = {"list_address": addresses}

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(
            path=BirdEyeApiUrls.TOKEN_METADATA_MULTIPLE, **request
        )

        return cast(dict, response)

    def market_data(self, address: str) -> dict:
        """Get market data of single token.

        :param address:       The address of the token.
        """
        params = {"address": address}

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(path=BirdEyeApiUrls.TOKEN_MARKET_DATA, **request)

        return cast(dict, response)

    def trade_data_single(self, address: str) -> dict:
        """Get trade data of single token

        :param addresses:       The address of the token.
        """
        params = {"address": address}

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(
            path=BirdEyeApiUrls.TOKEN_TRADE_DATA_SINGLE, **request
        )

        return cast(dict, response)

    @as_api_args
    def trade_data_multiple(self, addresses: str | list[str]) -> dict:
        """Get trade data of multiple tokens.

        :param addresses:       The address of the token...can be comma separated string or list of strings.
        """
        params = {"list_address": addresses}

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(
            path=BirdEyeApiUrls.TOKEN_TRADE_DATA_MULTIPLE, **request
        )

        return cast(dict, response)

    def holder(self, address: str, offset: int = 0, limit: int = 100) -> dict:
        """Get top holder list of the given token.

        :param address:     The address of the token.
        :param offset:      The offset.
        :param limit:       The limit.
        """
        params = {"address": address, "offset": offset, "limit": limit}

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(path=BirdEyeApiUrls.TOKEN_HOLDER, **request)

        return cast(dict, response)
