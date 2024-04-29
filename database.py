import sqlite3
import pandas as pd

def get_db():
    # Step 1: Read the CSV file into a DataFrame
    df = pd.read_csv('schemas/athlete_events.csv')

    # Step 2: Connect to the SQLite database and create it if it doesn't exist
    conn = sqlite3.connect('your_database.db')

    # Step 3: Write DataFrame to the database
    df.to_sql('table_name', conn, if_exists='replace', index=False)

    # Step 4: Perform queries
    cursor = conn.cursor()
    # cursor.execute("SELECT * FROM table_name WHERE condition")
    cursor.execute("SELECT * FROM table_name")
    rows = cursor.fetchall()
    # for row in rows:
    #     print(row)

    # Step 5: Close the connection
    # conn.close()

    return (cursor, conn)

def close_db(conn):
    conn.close()

def get_events_results_db():
    # Step 1: Read the CSV file into a DataFrame
    df = pd.read_csv('schemas/events_results.csv')

    # Step 2: Connect to the SQLite database and create it if it doesn't exist
    conn = sqlite3.connect('your_database.db')

    # Step 3: Write DataFrame to the database
    df.to_sql('events_results', conn, if_exists='replace', index=False)

    # Step 4: Perform queries
    cursor = conn.cursor()
    # cursor.execute("SELECT * FROM table_name WHERE condition")
    cursor.execute("SELECT * FROM events_results")
    rows = cursor.fetchall()

    # for row in rows:
    #     print(row)

    # Step 5: Close the connection
    # conn.close()

    return (cursor, conn)

def get_athlete_information_db():
    # Step 1: Read the CSV file into a DataFrame
    df = pd.read_csv('schemas/athlete_information.csv')

    # Step 2: Connect to the SQLite database and create it if it doesn't exist
    conn = sqlite3.connect('your_database.db')

    # Step 3: Write DataFrame to the database
    df.to_sql('athlete_information', conn, if_exists='replace', index=False)

    # Step 4: Perform queries
    cursor = conn.cursor()
    # cursor.execute("SELECT * FROM table_name WHERE condition")
    cursor.execute("SELECT * FROM athlete_information")
    rows = cursor.fetchall()

    # for row in rows:
    #     print(row)

    # Step 5: Close the connection
    # conn.close()

    return (cursor, conn)