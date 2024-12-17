import functools
from typing import Any, Callable


def as_api_args(func: Callable) -> Callable:
    """decorator to convert arguments to format expected by API

    boolean values are converted to lowercase strings
    list values are converted to comma-separated strings
    """

    @functools.wraps(func)
    def wrapper_as_api_args(*args: int, **kwargs: Any) -> Any:
        # check in **kwargs for lists and booleans
        for kwarg in kwargs:
            value = kwargs[kwarg]

            # check if arg is list and convert it to comma-separated string
            if isinstance(value, list):
                value = ",".join(value)
            # check if arg is boolean and convert it to string
            elif isinstance(value, bool):
                value = str(value).lower()

            kwargs[kwarg] = value

        return func(*args, **kwargs)

    return wrapper_as_api_args


def temp_remove_x_chain_header(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(self: Any, *args: int, **kwargs: Any) -> Any:
        # Temporarily remove the "x-chain" header
        original_headers = self.http.s.headers.copy()
        if "x-chain" in self.http.s.headers:
            del self.http.s.headers["x-chain"]

        try:
            # Call the original function
            result = func(self, *args, **kwargs)
        finally:
            # Re-add the "x-chain" header
            self.http.s.headers.update(original_headers)

        return result

    return wrapper
