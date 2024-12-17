from .defi import DeFi
from .pair import Pair
from .search import Search
from .token import Token
from .trader import Trader


RESOURCE_MAP = {
    "defi": DeFi,
    "token": Token,
    "trader": Trader,
    "pair": Pair,
    "search": Search,
}
