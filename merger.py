"""
AI model merger for weighted merge.

This is an algorithm that allows one to specify the models and their weights
such that they can be used in another algorithm to merge them two by two and
have each model appear in the total merged model in the requested percentages.

Example:

    input: {"model a": 0.25, "model b": 0.25, "model c": 0.50}
    output: same as input


NOTE:
    This is merely the algorithm that should be used, it is up to those
    attempting to create AI images to apply this to their scripts by taking out
    the portion that is saving the information into merged_models.
"""


def merge(models_and_percentages: dict[str, float]) -> dict[str, float]:
    """Merges the models together to come to the same percentages given."""

    sorted_model_names: list[str] = sorted(
        models_and_percentages,
        key=lambda key: models_and_percentages[key],
        reverse=True,
    )

    starting_model_name: str = sorted_model_names[0]

    # Initializing our mixes with our first model at 100% intensity.
    merged_models: dict[str, float] = {starting_model_name: 1.0}

    # This is going to allow us to know how much of the total we have
    # merged. This is going to inform the amount that we should be
    # adding of any one model.
    total_merged_percent: float = models_and_percentages[starting_model_name]

    for index in range(1, len(sorted_model_names)):
        current_model_name: str = sorted_model_names[index]
        current_model_percentage: float = models_and_percentages[current_model_name]

        total_merged_percent += current_model_percentage

        # This reduction amount is the space that is made for the new model
        # in the mix of the other models. For instance, if we are merging
        # the second model where both are the same intensity, then they
        # would mix at 50/50, which would mean reduction_in_weights = 0.5
        reduction_in_weights: float = current_model_percentage / total_merged_percent

        # Alpha is the nomenclature given by the logic problem as it was given
        # to me. This is the amount that model A is 'mixed' with model B,
        # essentially the opposite of the reduction.
        alpha: float = 1.0 - reduction_in_weights

        # Here's where we're going to perform the "merge".
        # What's happening is that we're going to reduce the percentages of all
        # already merged models by the reduction amount. Afterwards, we will
        # add the new model at its intensity.
        for model_name in merged_models:
            merged_models[model_name] = round(merged_models[model_name] * alpha, 2)
        merged_models[current_model_name] = reduction_in_weights

    return merged_models


if __name__ == "__main__":
    print(merge({"model a": 0.20, "model b": 0.30, "model c": 0.20, "model d": 0.30}))
