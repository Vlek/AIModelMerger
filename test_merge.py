import pytest
import merger


@pytest.mark.parametrize(
    "models_and_percentages",
    [
        ({"model a": 0.50, "model b": 0.50}),
        ({"model a": 0.90, "model b": 0.10}),
        ({"model a": 0.25, "model b": 0.25, "model c": 0.50}),
        ({"model a": 0.33, "model b": 0.33, "model c": 0.34}),
        ({"model a": 0.25, "model b": 0.25, "model c": 0.25, "model d": 0.25}),
        ({"model a": 0.20, "model b": 0.30, "model c": 0.20, "model d": 0.30}),
        (
            {
                "model a": 0.55,
                "model b": 0.15,
                "model c": 0.15,
                "model d": 0.10,
                "model e": 0.05,
            }
        ),
    ],
)
def test_merge_models(models_and_percentages) -> None:
    """"""
    merged_models: dict[str, float] = merger.merge(models_and_percentages)

    assert merged_models == models_and_percentages
