"""

"""


def give_time_estimate(models_and_percentages) -> None:
    """
    Prints the amount of time that it's likely to take to merge.

    For every merge, it takes roughly 2 minutes. Calculate how
    many merges need to be done and then output mergecount by the
    number of minutes.


    Expecting:
        10 models -> 5 + 3 + 2 + 1 merges -> 11 merges -> 22 minutes
    """
    ...


def merge_models(a: str, b: str, alpha: float) -> None:
    """Pretends to merge models, outputs info."""
    print(f"Merging model {a} with model {b} with alpha {alpha * 100}%")


def merge(models_and_percentages: dict[str, float]) -> dict[str, float]:
    """Merges the models together to come to the same percentages given."""
    sorted_models = sorted(
        models_and_percentages, key=lambda key: models_and_percentages[key]
    )

    # This is going to allow us to know how much of the total we have
    # merged. This is going to inform the amount that we should be
    # adding of any one model.
    total_merged: int = 0

    # TODO: Double-check this works for odds.
    for index in range(0, len(sorted_models) - 1, 2):
        model_name: str = sorted_models[index]

        print(f"Index: {index}, Model name: {model_name}")


if __name__ == "__main__":

    # merge_models("model a", "model b", 0.90)

    merge({"model a": 0.20, "model b": 0.30, "model c": 0.20, "model d": 0.30})
