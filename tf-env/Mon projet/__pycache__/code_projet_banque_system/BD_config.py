#from mysql.connector import connect
import mysql.connector


def connect():
   return mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'Bank_System'
    )
