import pandas as pd

from app.pipeline.transform import concat_to_dataframe

""""
Testar a concatenação das listas dos dataframes com pytest

"""
df1 = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
df2 = pd.DataFrame({"col1": [5, 6], "col2": [7, 8]})


def testar_concatenacao_dos_dataframes():
    # arrange
    data_frame_list = [df1, df2]
    data_frame = pd.concat(data_frame_list, ignore_index=True)

    # act
    df = concat_to_dataframe(data_frame_list)

    # assert
    assert data_frame.equals(df)
