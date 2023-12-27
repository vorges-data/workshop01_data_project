import os

import pandas as pd


def load_excel(data_frame: pd.DataFrame, output_path: str, file_name: str) -> str:
    """
    ecebe um dataframe e salva em arquivo excel

    args:
        data_frame (pd.DataFrame): dataframe a ser salvo como excel
        output_path (str): caminho do arquivo de saída
        file_name (str): nome do arquivo de saída

    return: "Arquivo salvo com sucesso!"

    """

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # salva o arquivo excel
    data_frame.to_excel(f"{output_path}/{file_name}.xlsx", index=False)

    # retorna a mensagem de sucesso
    return "Arquivo salvo com sucesso!"
