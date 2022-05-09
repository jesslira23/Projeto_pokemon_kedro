"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.0
"""

from kedro.pipeline import Pipeline, node, pipeline
from projeto_pokemon_kedro.pipelines.data_engineering.nodes import (
    enconde_target_variable,
    create_number_of_abilities_feature
)

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([

        node(   
            func = enconde_target_variable,
            inputs = "pp_pokemon_dataset",
            outputs = ["encode_pokemon_dataset", "label_encoder"],
            name = "enconde_target_variable"
        ),
        node(
            func = create_number_of_abilities_feature,
            inputs = "encode_pokemon_dataset",
            outputs = "pokemon_features",
            name = "create_number_of_abilities_feature"
        )
    ])
