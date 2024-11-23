from requests import Response


class BaseBirdEyeError(Exception):
    """Base class for exceptions in this module."""

    pass


class BirdEyeRequestError(BaseBirdEyeError):
    def __init__(self, message: str, response: Response) -> None:
        self.message = message

        super().__init__(message)

        self.response = response


class BirdEyeClientError(BaseBirdEyeError):
    pass
