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

    # TOKEN
    TOKEN_SECURITY = "defi/token_security"
    TOKEN_OVERVIEW = "defi/token_overview"
    TOKEN_CREATION_INFO = "defi/token_creation_info"
    TOKEN_TRENDING = "defi/token_trending"
    TOKEN_LIST_V2 = "/defi/v2/tokens/all"
    TOKEN_NEW_LISTING = "defi/v2/tokens/new_listing"
    TOKEN_TOP_TRADERS = "defi/v2/tokens/top_traders"
    TOKEN_ALL_MARKETS = "/defi/v2/markets"
    TOKEN_METADATA_SINGLE = "defi/v3/token/meta-data/single"
    TOKEN_METADATA_MULTIPLE = "defi/v3/token/meta-data/multiple"
    TOKEN_MARKET_DATA = "defi/v3/token/market-data"
    TOKEN_HOLDER = "defi/v3/token/holder"
    TOKEN_TRADE_DATA_SINGLE = "defi/v3/token/trade-data/single"
    TOKEN_TRADE_DATA_MULTIPLE = "defi/v3/token/trade-data/multiple"


class BirdEyeChainEnum(SimpleEnum):
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
