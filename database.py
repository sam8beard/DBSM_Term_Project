from flask import current_app, g 
import mysql.connector

def getdb(): 
    if 'db' not in g or not g.db.is_connected():
        g.db = mysql.conector.connect(
            host = current_app.config[''], # host name goes here 
            user = current_app.config[''], # username goes here 
            password = current_app.config[''], # password goes here  
            database = current_app.config[''], # database name goes here
            ssl_verify_identity=True, 
            ssl_ca='SSL/certs/ca-cert.pem'
        )
    return g.db 