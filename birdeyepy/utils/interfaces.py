import abc
from typing import Any


class IHttp(abc.ABC):
    """Interface for http requests libs"""

    @abc.abstractmethod
    def send(self, path: str, method: str = "get", **extra: Any) -> dict | list:
        raise NotImplementedError
