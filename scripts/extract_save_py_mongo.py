from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import requests
import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()


uri = os.getenv("MONGODB_URI")

def connection_mongo(uri):    
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    return client
def create_connect_db(client,db_name):
    db = client[db_name]
    return db
def create_connect_collection(db, col_name):
    collection = db[col_name]
    return collection
def extract_api_data(url):
    response = requests.get(url)
    return response
def insert_data(my_collection,response):
    try:
        docs = my_collection.insert_many(response.json())
        return docs
    except:
        print('error insert_data')
def visualize_collection(collection):
    try:
        for i in collection.find():
            print(i)
    except:
        print('error visualize collection')
def rename_column(my_collection, old_name, new_name):
    try:    
        my_collection.update_many({},{"$rename":{old_name:new_name}})
        return my_collection
    except:
        print('error rename column')
def select_category(collection, category):
    query = {"Categoria do Produto":category}
    lista_de_livros = []
    try:
        for i in collection.find(query):
            lista_de_livros.append(i)
        return lista_de_livros
    except:
        print('error select category')
def make_regex(collection, category, regex):
    try:
        query = {category :{"$regex": regex}}
        lista_produtos = []
        for i in collection.find(query):
            lista_produtos.append(i)
        return lista_produtos
    except:
        print('error make regex')
def create_dataframe(lista):
    try:
        df = pd.DataFrame(lista)
        return df
    except: 
        print('errr create dataframe')
def format_date(df,nome_campo_data):
    try:
        df_produtos_2021 = df
        
        df_produtos_2021[nome_campo_data] = pd.to_datetime(df_produtos_2021[nome_campo_data], format="%d/%m/%Y")

        df_produtos_2021[nome_campo_data] = df_produtos_2021[nome_campo_data].dt.strftime("%Y-%m-%d")
        
        return df_produtos_2021
    except:
        print("error format_date")
def generate_csv(df,path):
    #try:
    df.to_csv(path,index=False)
    return print(f"Arquivo gerado com sucesso >> {path}")
    #except:
    #    print("error generate_csv")
def close_connection(client):
    print('Fechando conecção...')
    client.close()


cliente = connection_mongo(uri)
my_db = create_connect_db(cliente,'my_db')
my_collection = create_connect_collection(my_db,'my_series2')
url_api = 'https://labdados.com/produtos'
resposta = extract_api_data(url_api)
docs = insert_data(my_collection, resposta)
print(len(docs.inserted_ids))
my_collection = rename_column(my_collection,'lat','Latitude')
#visualize_collection(my_collection)
list_for_category = select_category(my_collection,'livros')
print('Categorias Encontradas:\n',list_for_category[:5])
regex = "/202[1-9]"
list_for_regex = make_regex(my_collection,"Data da Compra",regex)
df = create_dataframe(list_for_regex)
df_with_date_format = format_date(df, "Data da Compra")
generate_csv(df_with_date_format,"data/produtos.csv")
close_connection(cliente)
