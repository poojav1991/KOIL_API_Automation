import configparser

import mysql.connector
from mysql.connector import Error

def getconfig():
    config = configparser.ConfigParser()
    config.read("utilities/properties.ini")
    return config
connect_config={
    'host' : getconfig()['DATABASE']['host'],
    'database' : getconfig()['DATABASE']['database'],
    'user' : getconfig()['DATABASE']['user'],
    'password' : getconfig()['DATABASE']['password']

}
def getConnection():
    try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print("Connection Successfully")
            return conn
    except Error as e:
        print(e)
def getQuery(query):
    conn= getConnection()
    cursor= conn.cursor()
    cursor.execute(query)
    row= cursor.fetchone()
    conn.close()
    return row
