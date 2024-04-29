from flask import Flask
import pandas as pd
import sqlite3
from database import get_db, get_events_results_db 
from markupsafe import Markup
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
    my_list = [['Name', 'Age', 'Country'],
           ['John', '25', 'USA'],
           ['Emily', '30', 'Canada'],
           ['David', '27', 'Australia']]

    html_table = list_to_html_table(my_list)
    # value = Markup(html_table)
    return render_template('index.html', dataToRender=html_table, dataToRender2=1) 

@app.route("/query1") 
def query1(): 
    (cursor, conn) = get_events_results_db()

    cursor.execute("SELECT * FROM events_results")
    rows = cursor.fetchall()
    counter = 0
    # print(type(rows))
    for row in rows:
        print(row)
        counter = counter + 1
        if (counter == 10):
            break
    # print(rows[1])
    # for i in range(0, 5):
    #     print(rows[i])

    data = rows[3]
    data2 = rows[4]
    my_list = [['Name', 'Age', 'Country'],
           ['John', '25', 'USA'],
           ['Emily', '30', 'Canada'],
           ['David', '27', 'Australia']]

    html_table = list_to_html_table(my_list)
    # value = Markup(html_table)
    return render_template('index.html', dataToRender=html_table, dataToRender2=1) 

def list_to_html_table(data):
    # Generate the table header
    table_html = '<table>\n<thead>\n<tr>'
    for header in data[0]:
        table_html += f'<th>{header}</th>'
    table_html += '</tr>\n</thead>\n'

    # Generate the table rows
    table_html += '<tbody>\n'
    for row in data[1:]:
        table_html += '<tr>'
        for value in row:
            table_html += f'<td>{value}</td>'
        table_html += '</tr>\n'
    table_html += '</tbody>\n'

    # Close the table tag
    table_html += '</table>'

    return Markup(table_html)


# # Example usage
# my_list = [['Name', 'Age', 'Country'],
#            ['John', '25', 'USA'],
#            ['Emily', '30', 'Canada'],
#            ['David', '27', 'Australia']]

# html_table = list_to_html_table(my_list)
# print(html_table)



