"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.0
"""

from kedro.pipeline import Pipeline, node, pipeline
from kedro_projeto_pokemon_kedro.data_processing.nodes import preprocess_a


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([

        node(
            func = preprocess_a,
            inputs = "pokemon",
            outputs = "preprocessed_a",
            name = "preprocessed_a_nodes"
        )
    ])
