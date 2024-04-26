from flask import Flask
import pandas as pd
import sqlite3
from database import get_db
app = Flask(__name__)

@app.route("/")
def home(): 
    (cursor, conn) = get_db()

    cursor.execute("SELECT * FROM table_name")
    rows = cursor.fetchall()
    counter = 0
    print(type(rows))
    # for row in rows:
    #     print(row)
    print(rows[1])
    for i in range(0, 5):
        print(rows[i])


    return "<h1> {{rows}} </h1>"
