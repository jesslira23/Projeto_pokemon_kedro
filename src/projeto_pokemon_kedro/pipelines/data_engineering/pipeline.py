"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.0
"""

from kedro.pipeline import Pipeline, node, pipeline
from projeto_pokemon_kedro.pipelines.data_engineering.nodes import enconde_target_variable


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([

        node(   
            func = enconde_target_variable,
            inputs = "pp_pokemon_dataset",
            outputs = ["encode_pokemon_dataset", "label_encoder"],
            name = "enconde_target_variable"
        )

    ])
