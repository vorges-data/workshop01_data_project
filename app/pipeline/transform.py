from typing import List

import pandas as pd

""""
Função para transformar uma lista de dataframes em um único dataframe

"""


def concat_to_dataframe(dataframes: List[pd.DataFrame]) -> pd.DataFrame:
    # concatena os dataframes da lista
    df = pd.concat(dataframes, ignore_index=True)

    # retorna o dataframe
    return df
