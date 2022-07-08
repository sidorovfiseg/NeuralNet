import psycopg2
from psycopg2 import OperationalError
import localdata_read as ldr


# Function which create connection with postgreSQL
# Функция, которая создает подключение к postgreSQL


def create_connection(db_name=None, db_user=None, db_password=None,
                      db_host=None, db_port=None):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        print("Connection to PostgreSQL DB successful")
        return execute_read_query(connection)
    except OperationalError as e:
        print(f"The error 'e' occurred, using local data_csv")
        return ldr.read_data_from_csv("resources/data.csv")


# Получение данных с помощью запросов
# Getting data from queries


def execute_read_query(connection, query=""):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error {e} occurred")
