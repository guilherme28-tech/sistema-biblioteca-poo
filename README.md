## Sistema de Biblioteca em Python

Projeto desenvolvido para praticar Programação Orientada a Objetos (POO) em Python, com foco em organização modular, controle de estado e persistência de dados.

## Descrição

Sistema para gerenciamento de biblioteca via terminal.

Permite cadastrar livros e usuários, realizar empréstimos e devoluções, listar registros e manter os dados salvos em arquivo JSON, preservando o estado do sistema mesmo após o encerramento da aplicação.

## Funcionalidades

Cadastro de livros

Cadastro de usuários

Empréstimo de livros

Devolução de livros

Listagem de livros

Listagem de usuários

Persistência automática de dados em JSON

Reconstrução automática dos empréstimos ao iniciar o sistema

Controle automático de IDs

## Estrutura do Projeto
sistema-biblioteca/

│

├── projeto_biblioteca/

│   ├── biblioteca.py

│   ├── livro.py

│   └── usuario.py

│

├── main.py

└── dados.json (gerado automaticamente)
## Conceitos aplicados

Classes e objetos

Encapsulamento

Organização modular

Serialização e desserialização de objetos

Manipulação de arquivos JSON

Controle de estado da aplicação

Reconstrução de relacionamentos entre objetos

Tratamento básico de exceções

## Requisitos

Python 3.10 ou superior

## Como executar
No terminal, dentro da pasta do projeto:

execute o arquivo "main.py"

Ao iniciar o programa, os dados serão carregados automaticamente do arquivo dados.json, caso ele exista.

## Persistência de Dados

Os dados do sistema são armazenados em um arquivo JSON.

Durante o encerramento ou atualização de registros:

As informações são convertidas para dicionários.

São salvas em arquivo.

Ao reiniciar o sistema, os objetos são reconstruídos a partir dos dados salvos.

Isso garante que livros, usuários e empréstimos sejam preservados entre execuções.

## Melhorias futuras

Implementação de testes automatizados

Migração para banco de dados relacional

Criação de API para acesso externo

Separação da camada de persistência

Interface gráfica ou interface web
