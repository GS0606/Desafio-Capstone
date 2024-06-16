# Desafio-Cosplam 
### Tem como finalidade verificar conhecimentos tecnicos de desenvolvimento Back-end.

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


