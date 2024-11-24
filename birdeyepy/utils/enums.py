class SimpleEnum:
    @classmethod
    def all(cls) -> list[str]:
        return [v for k, v in cls.__dict__.items() if not k.startswith("__")]


class BirdEyeApiUrls:
    # DEFI
    DEFI_PRICE = "defi/price"
    DEFI_TOKEN_LIST = "defi/tokenlist"
    DEFI_HISTORY_PRICE = "defi/history_price"

    # TRADER
    TRADER_GAINERS_LOSERS = "trader/gainers-losers"
    TRADER_SEEK_BY_TIME = "trader/txs/seek_by_time"


class BirdEyeChain(SimpleEnum):
    # Solana
    SOLANA = "solana"
    ETHEREUM = "ethereum"
    BSC = "bsc"
    AVALANCHE = "avalanche"
    ARBITRUM = "arbitrum"
    OPTIMISM = "optimism"
    POLYGON = "polygon"
    BASE = "base"
    ZKSYNC = "zksync"
    SUI = "sui"
