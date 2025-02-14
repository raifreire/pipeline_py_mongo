# PIPELINE COM PYTHON, MONGO, MYSQL.  <div align="center">
  <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
  <img src="[![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?logo=mongodb&logoColor=white)](#)">
  <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
</div>


## EXPLICAÇÃO DO CÓDIGO 🧑‍💻

* Exemplo de como conectar-se a um banco de dados MongoDB, 
* extrair dados de uma API, 
* inserir esses dados no banco de dados, 
* realizar algumas operações de manipulação e, 
* exportar os dados para um arquivo CSV. 
* pymongo para interagir com o MongoDB e carregar dados, 
* requests para fazer requisições HTTP, 
* pandas para manipulação de dados 
* dotenv para carregar variáveis de ambiente
* mysql para carregar dados em um banco relacional.

1. Importar as bibliotecas necessárias no arquivo `requirements.txt`
2. Carregar as variáveis de ambiente usando a função `load_dotenv()`
3. Obter a URI do MongoDB a partir das variáveis de ambiente e 
4. Criar conexão com o banco de dados MongoDB usando a classe MongoClient da biblioteca `pymongo`. 
 > A função `connection_mongo` é responsável por estabelecer essa conexão e verificar se a conexão foi bem-sucedida enviando um comando de ping ao servidor MongoDB.
5. Configurar uma conexão com um banco de dados MySQL usando Python.
6. Carregar dados de arquivos CSV e inserir esses dados em tabelas MySQL.
7. A primeira célula de código importa as bibliotecas necessárias: mysql.connector para a conexão com o MySQL.
8. A próxima célula de código estabelece a conexão com o banco de dados MySQL usando as credenciais armazenadas nas variáveis de ambiente (DB_HOST, DB_USERNAME, DB_PASSWORD).
9. A conexão é armazenada na variável cnx e é impressa para confirmar que a conexão foi bem-sucedida.
10. Em seguida, um cursor é criado a partir da conexão para executar comandos SQL.

* As funções create_connect_db e create_connect_collection são usadas para conectar-se a um banco de dados específico e a uma coleção dentro desse banco de dados, respectivamente. 
* A função extract_api_data faz uma requisição GET a uma URL fornecida e retorna a resposta. 
* A função insert_data insere os dados da resposta na coleção do MongoDB.
* A função visualize_collection, que imprime todos os documentos de uma coleção.
* A função rename_column, que renomeia uma coluna em todos os documentos de uma coleção.
* A função select_category, que seleciona documentos com base em uma categoria específica.
* A função make_regex, que seleciona documentos com base em uma expressão regular.
* A função create_dataframe, que cria um DataFrame do pandas a partir de uma lista de documentos.
* A função format_date, que formata uma coluna de data em um DataFrame.
* A função generate_csv, que exporta um DataFrame para um arquivo CSV.

  - Finalmente, o código principal executa essas funções em sequência para conectar-se ao banco de dados, extrair dados de uma API,
  - inserir esses dados no banco de dados, realizar algumas operações de manipulação e exportar os dados para um arquivo CSV.
  - A conexão com o banco de dados é fechada no final usando a função close_connection.
