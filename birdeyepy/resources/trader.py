from typing import Optional, cast

from birdeyepy.utils import BirdEyeApiUrls, BirdEyeRequestParams, IHttp


class Trader:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def gainers_losers(
        self,
        *,
        time_frame: Optional[str] = "1W",
        sort_by: Optional[str] = "PnL",
        sort_type: Optional[str] = "desc",
        offset: Optional[int] = 0,
        limit: Optional[int] = 10,
    ) -> list:
        """The API provides detailed information top gainers/losers

        :param time_frame: The time frame for the data (e.g., '24h', '7d').
        :param limit:      The number of results to return.
        """
        params = {
            "time_frame": time_frame,
            "sort_by": sort_by,
            "sort_type": sort_type,
            "offset": offset,
            "limit": limit,
        }

        request: BirdEyeRequestParams = {"params": params}
        response = self.http.send(path=BirdEyeApiUrls.TRADER_GAINERS_LOSERS, **request)

        return cast(list, response)

    def seek_by_time(
        self,
        *,
        address: str,
        tx_type: Optional[str] = "swap",
        sort_type: Optional[str] = "desc",
        offset: Optional[int] = 0,
        limit: Optional[int] = 100,
        before_time: Optional[int] = 0,
        after_time: Optional[int] = 0,
    ) -> dict:
        """Get list of trades of a trader with time bound option.

        :param address:             The address of the trader.
        :param tx_type:             The type of transaction.
        :param offset:              The offset.
        :param limit:               The limit.
        :param before_time:         Specify the time seeked before using Unix timestamps in seconds
        :param after_time:          Specify the time seeked after using Unix timestamps in seconds
        """
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
        response = self.http.send(path=BirdEyeApiUrls.TRADER_SEEK_BY_TIME, **request)

        return cast(dict, response)
