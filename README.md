# Script para Preenchimento de Banco de Dados com Faker

Este script Python foi desenvolvido para preencher um banco de dados MySQL com dados fictícios gerados pelo Faker. Ele gera títulos e descrições aleatórios para perguntas, que podem ser usados para população de bancos de dados para testes, desenvolvimento ou qualquer outro propósito que exija dados de exemplo.

## Breve Descrição

O script utiliza a biblioteca Faker para gerar dados fictícios realistas. Os dados gerados incluem títulos de perguntas e descrições correspondentes. Após a geração dos dados, eles são inseridos em uma tabela chamada "perguntas" em um banco de dados MySQL.

## Pré-requisitos

Antes de executar o script, é necessário ter o Python instalado no seu sistema. Além disso, você precisará das seguintes bibliotecas Python:

- faker
- mysql-connector-python

Você pode instalar essas bibliotecas usando o pip:

```
pip install Faker mysql-connector-python

```

## Configuração

Antes de executar o script, certifique-se de editar as configurações de conexão MySQL no arquivo `script.py`. Você precisará especificar o host, usuário, senha e nome do banco de dados MySQL ao qual deseja se conectar.

## Execução

Para executar o script, use o seguinte comando no terminal:

```
python script.py

```


