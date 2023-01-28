import pytest
import merger


@pytest.mark.parametrize(
    "models_and_percentages",
    [
        ({"model a": 50, "model b": 50}),
        ({"model a": 90, "model b": 10}),
        ({"model a": 25, "model b": 25, "model c": 50}),
        ({"model a": 33, "model b": 33, "model c": 34}),
    ],
)
def test_merge_models(models_and_percentages) -> None:
    """"""
    ...
