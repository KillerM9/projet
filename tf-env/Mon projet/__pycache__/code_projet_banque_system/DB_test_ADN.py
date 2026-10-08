import mysql.connector

def connect():
    return mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        database = 'Data_base_hospital'
    )