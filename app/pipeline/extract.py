"""Esse é o modelo de extração dos dados, que é a primeira etapa do pipeline."""

import glob  # biblioteca para listar arquivos de uma pasta
import os  # biblioteca para manipular arquivos e pastas
from typing import List  # biblioteca para definir tipos de variáveis

import pandas as pd  # biblioteca para manipular dataframes


def extract_from_excel(path: str) -> List[pd.DataFrame]:

    """
        Função para ler os arquivos de uma pasta data/input
        e retornar um dataframe com os dados

        args:
            input_path (str): caminho da pasta com os arquivos de entrada
            return list: dataframe com os dados dos arquivos
    """

    # lista com os arquivos da pasta
    all_files = glob.glob(os.path.join(path, '*.xlsx'))

    # lista com os dataframes de cada arquivo
    dataframes = []

    # itera sobre os arquivos
    for file in all_files:
        # lê o arquivo e adiciona na lista de dataframes
        dataframes.append(pd.read_excel(file))

    # retorna a lista de dataframes
    return dataframes


if __name__ == '__main__':
    # chama a função para ler os arquivos
    dataframes = extract_from_excel(path='data/input')
    print(dataframes)
