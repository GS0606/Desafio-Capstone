<<<<<<< HEAD
# Desafio-Cosplam
 Aplicação Flask seguindo a arquitetura MVC para buscar e exibir notícias da API Bloomberg.

## Módulo app_routes
Este repositório contém uma API simples baseada em Flask para buscar artigos de notícias com base em certos parâmetros, como tema, data de início, data de término e número da página.

### Visão Geral
A API possui um endpoint '/' que aceita requisições GET e retorna uma resposta JSON contendo artigos de notícias. Os dados são buscados usando o módulo service_news_service, que lida com a lógica de negócios para buscar e processar artigos de notícias.

### Endpoint
GET /
Busca artigos de notícias com base nos parâmetros fornecidos.

### Parâmetros:

'theme' : O tema ou categoria das notícias a serem buscadas.
'start_time' : A data de início para os artigos de notícias.
'end_time' : A data de término para os artigos de notícias.
'page' (opcional, padrão=1): O número da página para paginação.

### Exemplo de Requisição:
 GET http://127.0.0.1:3000/fetch?theme=brasil, corruption, semiconductors&page=1&day=June 17, 2024

### Exemplo de Resposta:
 {
    "artigos": [
        {
            "titulo": "Artigo Exemplo",
            "descricao": "Esta é uma descrição de exemplo de um artigo.",
            "publicado_em": "2023-01-15T12:00:00Z",
            "url": "http://exemplo.com/artigo"
        },
        ...
    ],
    "pagina": 2,
    "total_paginas": 5,
    "total_resultados": 50
}


## Módulo service_news_service
 O módulo service_news_service contém a função get_news_service, que é responsável por buscar e processar os artigos de notícias com base nos parâmetros fornecidos.

### Exemplo de Uso:
 from service_news_service import service_news_service

tema = "tecnologia"
data_inicio = "2023-01-01"
data_fim = "2023-01-31"
pagina = 2

dados = service_news_service.get_news_service(tema, data_inicio, data_fim, pagina)
print(dados)

##  Módulo storage_news_storage
 Este repositório contém um script Python para buscar artigos de notícias do Bloomberg com base em parâmetros específicos como tema, data de início, data de término e número da página.

### Visão Geral
 O função fetch_news usa a biblioteca requests para fazer uma requisição GET para a API de busca do Bloomberg. Os resultados são salvos em um arquivo JSON local e retornados como um dicionário Python.

### Armazenamento da Resposta
 A resposta da API é salva em um arquivo chamado response.json no diretório atual. O conteúdo do arquivo é formatado com indentação para facilitar a leitura.

##  Módulo storage_news_storage
 Este repositório contém um módulo Python que serve como uma camada de serviço para buscar artigos de notícias utilizando uma função de armazenamento (fetch_news). O módulo fornece uma interface simples para obter notícias com base em tema, data de início, data de término e número da página.

### Visão Geral
 A classe service_news_service fornece um método estático get_news_service que chama a função fetch_news do módulo storage_news_storage para buscar e retornar artigos de notícias.

##  Módulo main 
 Este repositório contém um aplicativo Flask que serve uma API para buscar artigos de notícias com base em tema, data de início, data de término e número da página. O aplicativo utiliza módulos personalizados para lidar com a lógica de negócios e o armazenamento dos dados.

### Visão Geral
 O aplicativo Flask é iniciado a partir do módulo 'app_runner.py', que importa a instância do aplicativo a partir do módulo 'app_routes.py'. O aplicativo está configurado para rodar na porta 3000.


=======
# Desafio-Cosplam 
### Tem como finalidade verificar conhecimentos técnicos de desenvolvimento Back-end.

## Funcionalidades
### Busca de Notícias: Permite buscar notícias de um tema ou data específico em um intervalo de tempo.

## Estrutura do Projeto
### Estrutura do projeto, mostrando os principais arquivos e diretórios:

projeto/
├── app.py               # Arquivo principal da aplicação Flask
├── service_news_service.py  # Módulo que contém o serviço para obter notícias
├── storage_news_storage.py  # Módulo para armazenamento de notícias
├── README.md            # Este arquivo README
└── ...

## Tecnologias Utilizadas

### Linguagem de Programação

**Python**

### Ferramentas de Desenvolvimento

 **Postman**: Utilizado para testar as requisições HTTP.
 
 **Flask**: Framework web utilizado para criar a aplicação.

## Exemplo de Uso
### Execute o arquivo app.py:
  python app.py
  Acesse http://127.0.0.1:3000 no seu navegador para buscar notícias.
### Execute no Postman o caminho:
  GET/page=1&theme=sports&start_time=2001-06-11&end_time=2002-06-12
>>>>>>> 59a0048b20a1be9b02cc059952827527a22bc899


