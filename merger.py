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


def merge(models_and_percentages: dict[str, float]) -> dict[str, float]:
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

    merged_models: dict[str, float] = {}
    starting_model: str = sorted_models[0]

    # This is going to allow us to know how much of the total we have
    # merged. This is going to inform the amount that we should be
    # adding of any one model.
    total_merged_percent: float = models_and_percentages[starting_model]

    # Initializing our mixes with our first model at 100% intensity.
    merged_models[starting_model] = 1.0

    # For all other models after the first one,
    for index in range(1, len(sorted_models)):
        current_model_name: str = sorted_models[index]
        current_model_percentage: float = models_and_percentages[current_model_name]

        # print(f"Merging {current_model_name} with intensity {current_model_percentage}")

        total_merged_percent += current_model_percentage
        reduction_in_weights: float = current_model_percentage / total_merged_percent
        alpha: float = 1.0 - reduction_in_weights

        # print(f"Reduction in weights: {reduction_in_weights}")
        # print(f"Total merged at this point: {total_merged_percent}")
        # print(f"This will reduce current weights by {alpha}")

        # Here's where we're going to perform the "merge".
        # What's happening is that we're going to reduce the percentages of all
        # already merged models by the reduction amount. Afterwards, we will
        # add the new model at its intensity.
        for model_name in merged_models:
            merged_models[model_name] = round(merged_models[model_name] * alpha, 2)
        merged_models[current_model_name] = reduction_in_weights

        # print(f"Current model weights: {merged_models}")

    return merged_models


if __name__ == "__main__":

    # merge_models("model a", "model b", 0.90)

    print(merge({"model a": 0.20, "model b": 0.30, "model c": 0.20, "model d": 0.30}))
