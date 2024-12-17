from typing import cast

from birdeyepy.utils import BirdEyeApiUrls, BirdEyeRequestParams, IHttp, as_api_args


class Pair:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    @as_api_args
    def overview_multiple(
        self,
        *,
        list_address: list[str],
    ) -> dict:
        """Get overview of multiple pairs.

        :param list_address:        A list of addresses
        """
        params = {"list_address": list_address}
        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(path=BirdEyeApiUrls.PAIR_OVERVIEW_MULTIPLE, **request)

        return cast(dict, response)

    @as_api_args
    def overview_single(
        self,
        *,
        address: str,
    ) -> dict:
        """Get overview of single pair

        :param list_address:        A list of addresses
        """
        params = {"address": address}
        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(path=BirdEyeApiUrls.PAIR_OVERVIEW_SINGLE, **request)

        return cast(dict, response)
