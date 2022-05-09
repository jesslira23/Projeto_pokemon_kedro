"""
This is a boilerplate test file for pipeline 'pre_processing'
generated using Kedro 0.18.0.
Please add your pipeline tests here.

Kedro recommends using `pytest` framework, more info about it can be found
in the official documentation:
https://docs.pytest.org/en/latest/getting-started.html
"""


import pandas as pd
from projeto_pokemon_kedro.pipelines.pre_processing.nodes import pre_processing

def test_processing_expectations():
    test_dataset = pd.DataFrame({
        "name": ["Charmander", "Bulbasaur", None],
        "generation": [1, 2, 3],
        "type2": [True, False, True]
    })

    output = pre_processing(test_dataset, selected_generation=[1])

    assert output.equals(
        pd.DataFrame({
            "name": ["Charmander"],
            "generation": ['1']
        })
    )