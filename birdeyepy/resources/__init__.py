from .defi import DeFi
from .token import Token
from .trader import Trader


RESOURCE_MAP = {
    "defi": DeFi,
    "token": Token,
    "trader": Trader,
}
