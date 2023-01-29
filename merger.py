"""

"""

import math


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


def merge(models_and_percentages: dict[str, int]) -> dict[str, int]:
    """Merges the models together to come to the same percentages given."""

    # We're going to sort in reverse order in the hopes that the smaller
    # percentages are not crowded out via rounding. The ones with the
    # higher percentages can take a rounding hit without as much effect
    # by definition.
    sorted_models = sorted(
        models_and_percentages,
        key=lambda key: models_and_percentages[key],
        reverse=True,
    )

    merged_models: dict[str, int] = {}
    starting_model: str = sorted_models[0]

    # This is going to allow us to know how much of the total we have
    # merged. This is going to inform the amount that we should be
    # adding of any one model.
    total_merged_percent: int = models_and_percentages[starting_model]

    # Initializing our mixes with our first model at 100% intensity.
    merged_models[starting_model] = 100

    # For all other models after the first one,
    for index in range(1, len(sorted_models)):
        current_model_name: str = sorted_models[index]
        current_model_percentage: int = models_and_percentages[current_model_name]

        print(
            f"Merging model {current_model_name} with intensity {current_model_percentage}"
        )

        total_merged_percent += current_model_percentage
        reduction_in_weights: int = math.floor(
            current_model_percentage / total_merged_percent * 100
        )
        alpha: int = 100 - reduction_in_weights

        print(f"Total merged at this point: {total_merged_percent}")
        print(f"This will reduce current weights by {alpha}")

        # Here's where we're going to perform the "merge".
        # What's happening is that we're going to reduce the percentages of all
        # already merged models by the reduction amount. Afterwards, we will
        # add the new model at its intensity.
        for model_name in merged_models:
            merged_models[model_name] = math.floor(
                merged_models[model_name] * (alpha / 100)
            )
        merged_models[current_model_name] = reduction_in_weights

    return merged_models


if __name__ == "__main__":

    # merge_models("model a", "model b", 0.90)

    print(merge({"model a": 20, "model b": 30, "model c": 20, "model d": 30}))
