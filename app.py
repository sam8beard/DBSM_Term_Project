from flask import Flask, g
import pandas as pd
import sqlite3
from database import setup_db
from markupsafe import Markup
from flask import render_template
app = Flask(__name__)

# def get_db():
#     if 'db' not in g:
#         g.db = sqlite3.connect('olympics_database.db')
#     return g.db

# @app.teardown_appcontext
# def teardown_db(exception):
#     db = g.pop('db', None)
#     print("Test Debug")
#     if db is not None:
#         db.close()

@app.route("/")
def home(): 
    # (cursor, conn) = get_db()
    conn = sqlite3.connect('olympics_database.db')
    print("Connection Created")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM athlete_information Limit 100")
    rows = cursor.fetchall()
    conn.close()
    print("Query Executed \nConnection Closed")

    # for row in rows:
    #     print(row)

    my_list = [['Name', 'Age', 'Country'],
           ['John', '25', 'USA'],
           ['Emily', '30', 'Canada'],
           ['David', '27', 'Australia']]

    html_table = list_to_html_table(my_list)
    # value = Markup(html_table)
    return render_template('index.html', dataToRender=html_table, dataToRender2=1) 

@app.route("/query1") 
def query1(): 
    # cursor.execute("SELECT ID, GAMES FROM athlete_information LIMIT 100")
    # rows = [['ID','Games','Name','Sex','Age','Height','Weight','NOC']] + cursor.fetchall()
    
    conn = sqlite3.connect('olympics_database.db')
    print("Connection Created")
    sql_query = """
    SELECT Games,
        SUM(CASE WHEN Sex = 'M' THEN 1 ELSE 0 END) AS Male_Athletes,
        SUM(CASE WHEN Sex = 'F' THEN 1 ELSE 0 END) AS Female_Athletes
    FROM athlete_information
    GROUP BY Games;
    """
    cursor = conn.cursor()
    cursor.execute(sql_query)
    rows = [['Games', 'Num Male Athletes', 'Num Female Athletes']] + cursor.fetchall()
    conn.close()
    print("Query Executed \nConnection Closed")


    # counter = 0
    # for row in rows:
    #     print(row)
    #     counter += 1
    #     if (counter == 10):
    #         break

    html_table = list_to_html_table(rows)
    # value = Markup(html_table)
    return render_template('query1.html', dataToRender=html_table, dataToRender2=1) 

@app.route("/query2") 
def query2(): 
    conn = sqlite3.connect('olympics_database.db')
    print("Connection Created")
    cursor = conn.cursor()


    # cursor.execute("SELECT * FROM events_results LIMIT 100")

    # query to find countries with the most medals won between 1980 and 1990
    query = """
    SELECT 
        nr.region AS Country,
        COUNT(er.Medal) AS Total_Medals_Won
    FROM 
        athlete_information AS ai
    JOIN 
        events_results AS er ON ai.ID = er.ID AND ai.Games = er.Games
    JOIN 
        noc_regions AS nr ON ai.NOC = nr.NOC
    WHERE 
        er.Medal IS NOT NULL AND er.Medal != 'NA'
        AND SUBSTRING(er.Games, 1, 4) BETWEEN '1980' AND '1990'
    GROUP BY 
        nr.region
    ORDER BY 
        Total_Medals_Won DESC;
    """

    cursor.execute(query)
    rows = [['Country', 'Medals Won (1980 - 1990)']] + cursor.fetchall()

    # query to find countries with the most medals won between 1990 and 2000
    query = """
    SELECT 
        nr.region AS Country,
        COUNT(er.Medal) AS Total_Medals_Won
    FROM 
        athlete_information AS ai
    JOIN 
        events_results AS er ON ai.ID = er.ID AND ai.Games = er.Games
    JOIN 
        noc_regions AS nr ON ai.NOC = nr.NOC
    WHERE 
        er.Medal IS NOT NULL AND er.Medal != 'NA'
        AND SUBSTRING(er.Games, 1, 4) BETWEEN '1990' AND '2000'
    GROUP BY 
        nr.region
    ORDER BY 
        Total_Medals_Won DESC;
    """

    cursor.execute(query)
    rows2 = [['Country', 'Medals Won (1990 - 2000)']] + cursor.fetchall()

    # query to find countries with the most medals won between 2000 and 2010
    query = """
    SELECT 
        nr.region AS Country,
        COUNT(er.Medal) AS Total_Medals_Won
    FROM 
        athlete_information AS ai
    JOIN 
        events_results AS er ON ai.ID = er.ID AND ai.Games = er.Games
    JOIN 
        noc_regions AS nr ON ai.NOC = nr.NOC
    WHERE 
        er.Medal IS NOT NULL AND er.Medal != 'NA'
        AND SUBSTRING(er.Games, 1, 4) BETWEEN '2000' AND '2010'
    GROUP BY 
        nr.region
    ORDER BY 
        Total_Medals_Won DESC;
    """

    cursor.execute(query)
    rows3 = [['Country', 'Medals Won (2000 - 2010)']] + cursor.fetchall()

    # query to find countries with the most medals won between 2000 and 2010
    query = """
    SELECT 
        nr.region AS Country,
        COUNT(er.Medal) AS Total_Medals_Won
    FROM 
        athlete_information AS ai
    JOIN 
        events_results AS er ON ai.ID = er.ID AND ai.Games = er.Games
    JOIN 
        noc_regions AS nr ON ai.NOC = nr.NOC
    WHERE 
        er.Medal IS NOT NULL AND er.Medal != 'NA'
        AND SUBSTRING(er.Games, 1, 4) BETWEEN '2010' AND '2016'
    GROUP BY 
        nr.region
    ORDER BY 
        Total_Medals_Won DESC;
    """

    cursor.execute(query)
    rows4 = [['Country', 'Medals Won (2010 - 2016)']] + cursor.fetchall()

    conn.close()
    print("Query Executed \nConnection Closed")


    html_table = list_to_html_table(rows)
    html_table2 = list_to_html_table(rows2)
    html_table3 = list_to_html_table(rows3)
    html_table4 = list_to_html_table(rows4)
    # value = Markup(html_table)
    return render_template('query2.html', dataToRender=html_table, dataToRender2=html_table2, dataToRender3=html_table3,
                           dataToRender4=html_table4) 


@app.route("/query3") 
def query3(): 
# cursor.execute("SELECT ID, GAMES FROM athlete_information LIMIT 100")
    # rows = [['ID','Games','Name','Sex','Age','Height','Weight','NOC']] + cursor.fetchall()
    
    conn = sqlite3.connect('olympics_database.db')
    print("Connection Created")

    # sql_query = """
    # SELECT 
    #     ai.NOC AS Country
    # FROM 
    #     athlete_information AS ai
    # LIMIT 100
    # """

    sql_query = """
    SELECT 
        ai.ID,
        ai.Name,
        GROUP_CONCAT(DISTINCT ai.Games) AS Olympics,
        GROUP_CONCAT(DISTINCT hc.City) AS Host_Cities
    FROM 
        athlete_information AS ai
    JOIN 
        events_results AS er ON ai.ID = er.ID
    JOIN 
        host_cities AS hc ON ai.Games = hc.Games
    WHERE 
        er.Medal IS NOT NULL AND er.Medal != 'NA'
        AND ai.ID IN (
            SELECT 
                ai.ID
            FROM 
                athlete_information AS ai
            JOIN 
                events_results AS er ON ai.ID = er.ID
            WHERE 
                er.Medal IS NOT NULL AND er.Medal != 'NA'
            GROUP BY 
                ai.ID
            HAVING 
                COUNT(DISTINCT ai.Games) > 1
        )
    GROUP BY 
        ai.ID, ai.Name
    ORDER BY 
        ai.ID
    LIMIT 1000
    """

    cursor = conn.cursor()
    cursor.execute(sql_query)
    rows = [['ID', 'Name', 'Olympics', 'Host_City']] + cursor.fetchall()
    conn.close()
    print("Query Executed \nConnection Closed")


    # sql_query = """
    # SELECT 
    #     ai.NOC AS Country,
    # FROM 
    #     athlete_information AS ai
    # LIMIT 100
    # """

    html_table = list_to_html_table(rows)
    # value = Markup(html_table)
    return render_template('query1.html', dataToRender=html_table, dataToRender2=1) 


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



