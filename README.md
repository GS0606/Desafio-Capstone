<<<<<<< HEAD
# Desafio-Cosplam
Esta aplicação é um serviço web simples baseado em Flask, projetado para contar e visualizar o número de postagens de notícias publicadas em um dia específico para vários temas. Ela processa arquivos JSON contendo dados de notícias e gera um histograma dos resultados.

### Tecnologias Utilizadas
Python: Linguagem de programação principal utilizada.\**
Flask: Framework leve para desenvolvimento de aplicações web WSGI.\**
Matplotlib: Biblioteca de plotagem utilizada para gerar o histograma.\**
Collections (Counter): Contêiner da biblioteca padrão do Python utilizado para contar a ocorrência de elementos.\**
OS: Módulo Python que fornece funcionalidades dependentes do sistema operacional.\**
JSON: Formato de intercâmbio de dados leve utilizado para manipulação de dados JSON.\**

### Estrutura da Aplicação

app = Flask(__name__): Inicializa a aplicação Flask.
count_posts_by_day(json_data, target_day): Função que conta o número de postagens publicadas em um dia específico.
/fetch: Endpoint principal da aplicação, que processa a requisição, conta as postagens de notícias pelos temas especificados, salva os resultados em um arquivo JSON e gera um histograma
\**
### Endpoints
/fetch
Descrição: Busca o número de postagens de notícias para os temas especificados em um determinado dia, salva os resultados em um arquivo JSON e gera um histograma.

Método: GET

Parâmetros:

day: Dia para o qual contar as postagens de notícias (formato: YYYY-MM-DD).
themes: Lista separada por vírgulas dos temas para contar as postagens de notícias.
Resposta: Objeto JSON contendo a contagem de postagens de notícias para cada tema.
\**
### Exemplo de Requisição:
curl "http://localhost:3000/fetch?day=2023-06-18&themes=brasil,corruption,semiconductors"

### Exemplo de Resposta:
{
    "brasil": 5,
    "corruption": 3,
    "semiconductors": 7
}
\**
## Como Executar a Aplicação

1-Clonar o Repositório:
git clone <url-do-repositorio>
cd <diretorio-do-repositorio>

2-Instalar Dependências: 

Certifique-se de ter Python instalado e, em seguida, instale os pacotes necessários usando pip:
pip install Flask matplotlib

3-Executar a Aplicação:
python histograma_generation.py

4-Acessar o Endpoint: Use uma ferramenta como Postman ou seu navegador web para enviar uma requisição GET para:

http://localhost:3000/fetch?day=2024-06-12&themes=brasil,corruption,semiconductors
\**
### Estrutura de Diretórios

news-fetcher/
├── api_files/
│   ├── brasil_1.json
│   ├── corruption_1.json
│   ├── semiconductors_1.json
│   └── ... (outros arquivos JSON)
├── output/
│   ├── histogram.png
│   └── news_data.json
├── histograma_generation.py: Arquivo principal da aplicação Flask.
.py
└── README.md
\**
Descrição dos Diretórios e Arquivos:

*news-fetcher/*: Diretório raiz do projeto.
*api_files/*: Diretório contendo os arquivos JSON com dados de notícias. Cada arquivo segue o formato <tema>_<número_da_página>.json.
*brasil_1.json*: Arquivo JSON com notícias sobre o tema "brasil".
*corruption_1.json*: Arquivo JSON com notícias sobre o tema "corruption".
*semiconductors_1.json*: Arquivo JSON com notícias sobre o tema "semiconductors".
*output/*: Diretório onde são salvos o arquivo JSON de saída e a imagem do histograma.
*histogram.png*: Imagem PNG contendo o histograma do número de postagens por tema.
*news_data.json*: Arquivo JSON contendo a contagem de postagens de notícias para cada tema.
*histograma_generation.py*: Arquivo principal da aplicação Flask.
*README.md*: Arquivo de documentação com informações sobre a aplicação, como instalar, executar e usar.
### Arquivos de Saída

*news_data.json*: Arquivo JSON contendo a contagem de postagens de notícias para cada tema.
*histogram.png*: Arquivo de imagem PNG contendo o histograma do número de postagens por tema.

### Tratamento de Erros
A aplicação verifica se o parâmetro day foi fornecido e retorna uma mensagem de erro se estiver ausente.
Ela lida com erros de decodificação JSON e os registra no console.
Ela garante que o diretório de saída exista antes de tentar salvar os arquivos.


