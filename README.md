# Projeto de estrutura de Dados ETL com python


## Sobre o Projeto
Este é um projeto em Python desenvolvido para facilitar a união de 50 planilhas Excel em um único arquivo, visando simplificar e agilizar o processo de ETL (Extração, Transformação e Carga) de dados.

### Objetivos do Projeto:
O principal objetivo deste projeto é fornecer uma solução eficiente para consolidar múltiplas planilhas Excel em um único arquivo, minimizando o tempo e esforço necessários para essa tarefa.

### Ferramentas utilizadas:
* **Poetry**: Gerenciador de dependências Python para a gestão do ambiente virtual e pacotes utilizados no projeto.
* **Pytest**: Framework de teste utilizado para garantir a qualidade e a integridade do código.
* **Mkdocs**: Utilizado para gerar a documentação do projeto de forma simples e organizada.
* **Git e Github**: Ferramentas de controle de versão e hospedagem do código fonte.

### Como utilizar?
Para utilizar este projeto, siga as instruções abaixo:

1. Clonagem do repositório:

```bash
git clone https://github.com/vorges-data/workshop01_data_project.git

cd workshop01_data_project
```

2. Configure a versão correta do Python:
```bash
pyenv install 3.11.3
pyenv local 3.11.3
```

3. Instale as dependências do Projeto:
```bash
poetry install
```

4. Ative o ambiente virtual:
```bash
poetry shell
```

5. Execute os teste para garantir que está funcionando:
```bash
task test
```

6. Execute o comando para executar a pipeline ETL:
```bash
task run
```

7. Ao executar a pipeline, verifique na pasta data/output se o arquivo foi gerado.

## Documentação Adicional
A documentação detalhada do projeto pode ser encontrada na pasta **docs** ou acessada [Aqui](https://github.com/vorges-data/workshop01_data_project), onde são descritos detalhes sobre a estrutura do projeto, sua utilização e outras informações relevantes.

## Contato
* **Vinicius Borges** - [vinicius.jborges36@gmail.com](mailto:vinicius.jborges36@gmail.com)