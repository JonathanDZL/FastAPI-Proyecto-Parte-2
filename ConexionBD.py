import mysql.connector

mysql_config ={
    'user':'root',
    'password':'',
    'host' : 'localhost',
    'database':'bs_transporte',
    'auth_plugin':''



}

connection = mysql.connector.connect(**mysql_config)

def get_connection():
    return connection