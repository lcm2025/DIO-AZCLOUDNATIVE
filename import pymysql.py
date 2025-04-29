import pymysql

try:
    connection = pymysql.connect(
        host="dbsrvlab001eastus.database.windows.net",
        user="adminlcm2025",
        password="ad2025@L",
        database="sqllab001dbdeveastus",
        ssl={"ssl": True},
        connect_timeout=30
    )
    print("Conexão bem-sucedida!")
except Exception as e:
    print(f"Erro: {e}")