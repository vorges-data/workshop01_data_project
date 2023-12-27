"""Esse é o modelo de transformação dos dados, que é a segunda etapa do pipeline."""
from typing import List

import pandas as pd


def concat_to_dataframe(dataframes: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Concatena uma lista de dataframes em um único dataframe.

    Args:
        dataframes (list): Lista de dataframes a serem concatenados.

    Returns:
        pandas.DataFrame: Um único dataframe resultante da concatenação.
    """

    # concatena os dataframes da lista
    df = pd.concat(dataframes, ignore_index=True)

    # retorna o dataframe
    return df
