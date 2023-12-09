from pipeline.extract import extract_from_excel


listas_dataframes = extract_from_excel(path="data/input")
print(listas_dataframes)