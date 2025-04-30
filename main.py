import streamlit as st
from azure.storage.blob import BlobServiceClient
import pymysql
import uuid

#Configurações do Azure Storage
CONNECTION_STRING = "Sua string de conexão"
CONTAINER_NAME = "Nome do container criado no Azure"
ACCOUNT_NAME = "Nome do storage criado"

#Configurações do Azure SQL Server
SQL_SERVER = "nome do servidor do banco criado no Azure"
SQL_DATABASE = "Nome do database criado no Azure"
SQL_USERNAME = "Nome do usuário (criado durante a criação do DB)"
SQL_PASSWORD = "senha do usuário criado"

#Título do App
st.title("Cadastro de Produto - E-Commerce na Cloud")

#Formulário para cadastro do produto
product_name = st.text_input("Nome do Produto")
description = st.text_area("Descrição do Produto")
price = st.number_input("Preço do Produto", min_value=0.0, format="%.2f")
upload_file = st.file_uploader("Imagem do Produto", type=["jpg", "jpeg", "png"])

#Função para enviar imagem para o Azure Blob Storage
def upload_image(file):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING, connection_verify=False)
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)
        #Cria um nome único para a imagem
        blob_name = f"{uuid.uuid4()}.jpg"
        blob_client = container_client.get_blob_client(blob_name)
        #Faz o upload da imagem
        blob_client.upload_blob(file.read(), overwrite=True)
        #Monta a URL de acesso à imagem
        image_url = f"https://{ACCOUNT_NAME}.blob.core.windows.net/{CONTAINER_NAME}/{blob_name}"
        return image_url
    except Exception as e:
        st.error(f"Erro ao enviar imagem: {e}")
        return None
    
# Função para inserir os dados do produto no Azure SQL Server usando o Pymssql
def insert_product_sql(product_data):
    try:
        connect = pymysql.connect(
            host=SQL_SERVER,
            user=SQL_USERNAME,
            password=SQL_PASSWORD,
            database=SQL_DATABASE,
            ssl={"ssl": True},
            connect_timeout=30
        )
        cursor = connect.cursor()
        #Insere os dados do produto
        insert_query = """
            INSERT INTO dbo.produtos (nome, descricao, preco, imagem_url)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_query, (product_data['name'], product_data['description'], product_data['price'], product_data['image_url']))
        connect.commit()
        cursor.close()
        return True
    except Exception as e:
        st.error(f"Erro ao inserir no Azure SQL: {e}")
        return False

#Função para listar os produtos do Azure SQL Server
def list_products_sql():
    try:
        connect = pymysql.connect(
            host=SQL_SERVER,
            user=SQL_USERNAME,
            password=SQL_PASSWORD,
            database=SQL_DATABASE,
            ssl={"ssl": True},
            connect_timeout=30
        )
        cursor = connect.cursor(as_dict=True)
        #Seleciona os produtos
        select_query = "SELECT id, nome, descricao, preco, imagem_url FROM dbo.produtos"
        cursor.execute(select_query)
        products = cursor.fetchall()
        cursor.close()
        return products
    except Exception as e:
        st.error(f"Erro ao listar produtos: {e}")
        return []
#Função para exibir a lista de produtos na tela
def lis_produtos_screen():
    products = list_products_sql()
    if products:
        cards_por_linha = 3
        colunas = st.columns(cards_por_linha)
        for i, product in enumerate(products):
            with colunas[i % cards_por_linha]:
                st.image(product['imagem_url'], width=150)
                st.write(f"**{product['nome']}**")
                st.write(f"Descrição: {product['descricao']}")
                st.write(f"Preço: R$ {product['preco']:.2f}")
                st.write("---")
                st.write(f"[Ver Produto](https://{ACCOUNT_NAME}.blob.core.windows.net/{CONTAINER_NAME}/{product['imagem_url']})")
            if (i + 1) % cards_por_linha == 0 and (i + 1) < len(products):
                colunas = st.columns(cards_por_linha)
    else:
        st.write("Nenhum produto cadastrado.")

#Botão para cadastro de produto
if st.button("Cadastrar Produto"):
    if not product_name or not description or price is None:
        st.warning("Preencha todos os campos obrigatórios!")
    else:
        #Envia a imagem (se houver) para o Azure Storage
        image_url = ""
        if upload_file is not None:
            image_url = upload_image(upload_file)

        #dados do produto
        product_data = {
            "nome": product_name,
            "descricao": description,
            "preco": price,
            "imagem_url": image_url
        }

        #Insere os dados no Azure SQL Server
        if insert_product_sql(product_data):
            st.success("Produto cadastrado com sucesso!")
            #Limpa os campos do formulário
            lis_produtos_screen()
        else:
            st.error("Erro ao cadastrar o produto. Tente novamente.")
        
st.header("Lista de Produtos")

#Botão para carregar e exibir a lista de produtos
if st.button("Listar Produtos"):
    lis_produtos_screen()
st.write("Clique no botão acima para listar os produtos cadastrados.")
