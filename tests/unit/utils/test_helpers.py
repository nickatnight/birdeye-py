from birdeyepy.utils.helpers import as_api_args


def test_as_api_args_with_list() -> None:
    # Arrange
    @as_api_args
    def uat_function(ids: str | list) -> None:
        assert ids == "a,b,c"

    # Assert
    uat_function(ids=["a", "b", "c"])
