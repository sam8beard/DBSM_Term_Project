from flask import Flask
import pandas as pd
import sqlite3
from database import get_db
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home(): 
    (cursor, conn) = get_db()

    cursor.execute("SELECT * FROM table_name")
    rows = cursor.fetchall()
    counter = 0
    # print(type(rows))
    # # for row in rows:
    # #     print(row)
    # print(rows[1])
    # for i in range(0, 5):
    #     print(rows[i])

    data = rows[3]
    data2 = rows[4]
    
    return render_template('index.html', dataToRender=data, dataToRender2=1) 

@app.route("/query1") 
def query1(): 
    return 


