"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline
from kedro_projeto_pokemon_kedro import data_processing


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """

    data_processing_pipeline = data_processing.create_pipeline()


    return {"__default__": pipeline([])}
