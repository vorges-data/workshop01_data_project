# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Workflow

```mermaid
flowchart LR
    subgraph ETL[Pipeline]
        A[Múltiplos Arquivos: Arquivos Excel] --> B[Extração: extract_from_excel]
        B[Extração: extract_from_excel] --> |Gera uma lista de Dataframes| C[Transformação: consolidate_dataframes] 
        C[Transformação: consolidate_dataframes] --> |Gera um Dataframe Consolidado| D[Carga: Converte para Excel]
        D[Carga: Converte para Excel] --> |Salva o consolidado em Excel| E[Pasta Output: Um arquivo único Excel]
       
    end
```


# Função de Extração de Dados
### ::: app.pipeline.extract.extract_from_excel

# Função de Tranformação de Dados
### ::: app.pipeline.transform.concat_to_dataframe