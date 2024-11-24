from .defi import DeFi
from .token import Token
from .trader import Trader
from .wallet import Wallet


RESOURCE_MAP = {
    "defi": DeFi,
    "token": Token,
    "trader": Trader,
    "wallet": Wallet,
}
