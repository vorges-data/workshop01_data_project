"""
Módulo principal responsável pela execução do script.
"""
from pipeline.extract import extract_from_excel
from pipeline.load import load_excel
from pipeline.transform import concat_to_dataframe


def main():
    """
    Função principal do script.
    Realiza a extração, transformação e carregamento dos dados.
    """

    # chama a função para ler os arquivos
    dataframes = extract_from_excel(path="data/input")
    print(type(dataframes))

    # chama a função para transformar os dataframes em um único dataframe
    df = concat_to_dataframe(dataframes)
    print(type(df))

    # chama a função para salvar o dataframe em um arquivo excel
    load_excel(data_frame=df, output_path="data/output", file_name="output")


if __name__ == "__main__":
    main()
