"""
This is a boilerplate pipeline 'pre_processing'
generated using Kedro 0.18.0
"""

from kedro.pipeline import Pipeline, node, pipeline
from projeto_pokemon_kedro.pipelines.pre_processing.nodes import pre_processing


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([

        node(   
            func = pre_processing,
            inputs = ["raw_pokemon_dataset", 'params:selected_generation'],
            outputs = "pp_pokemon_dataset",
            name = "pre_processed_pokemon"
        )

    ])