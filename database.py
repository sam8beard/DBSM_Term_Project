import sqlite3
import pandas as pd

def setup_db():
    # Step 1: Connect to SQL Database and create it if it doesn't exist
    conn = sqlite3.connect('olympics_database.py.db')

    # Step 2: Read the CSV files into Dataframes, and write them to database
    df = pd.read_csv('schemas/events_results.csv')
    df.to_sql('events_results', conn, if_exists='replace', index=False)
    df = pd.read_csv('schemas/athlete_information.csv')
    df.to_sql('athlete_information', conn, if_exists='replace', index=False)
    df = pd.read_csv('schemas/host_cities.csv')
    df.to_sql('host_cities', conn, if_exists='replace', index=False)
    df = pd.read_csv('schemas/noc_regions.csv')
    df.to_sql('noc_regions', conn, if_exists='replace', index=False)
    df = pd.read_csv('schemas/athlete_countries.csv')
    df.to_sql('athlete_countries', conn, if_exists='replace', index=False)

    # Step 3: Create cursor to perform queries
    # cursor = conn.cursor()

    # Can Run queries using cursor.excute() and cursor.fetchall():
    # cursor.execute(<some sql statement as a string>)
    # rows = cursor.fetchall()

    # Step 4: Close the connection --> We do this in another route
    conn.close()
    print("Database and tables created, stored in olympics_database.py.py")

    return (conn) 

def main():
    setup_db

if __name__ == "__main__":
    setup_db()

# def close_db(conn):
#     conn.close()

# def get_events_results_db():
#     # Step 1: Read the CSV file into a DataFrame
#     df = pd.read_csv('schemas/events_results.csv')

#     # Step 2: Connect to the SQLite database and create it if it doesn't exist
#     conn = sqlite3.connect('olympics_database.py.db')

#     # Step 3: Write DataFrame to the database
#     df.to_sql('events_results', conn, if_exists='replace', index=False)

#     # Step 4: Perform queries
#     cursor = conn.cursor()
#     # cursor.execute("SELECT * FROM table_name WHERE condition")
#     cursor.execute("SELECT * FROM events_results")
#     rows = cursor.fetchall()

#     # for row in rows:
#     #     print(row)

#     # Step 5: Close the connection
#     # conn.close()

#     return (cursor, conn)

# def get_athlete_information_db():
#     # Step 1: Read the CSV file into a DataFrame
#     df = pd.read_csv('schemas/athlete_information.csv')

#     # Step 2: Connect to the SQLite database and create it if it doesn't exist
#     conn = sqlite3.connect('olympics_database.py.db')

#     # Step 3: Write DataFrame to the database
#     df.to_sql('athlete_information', conn, if_exists='replace', index=False)

#     # Step 4: Perform queries
#     cursor = conn.cursor()
#     # cursor.execute("SELECT * FROM table_name WHERE condition")
#     cursor.execute("SELECT * FROM athlete_information")
#     rows = cursor.fetchall()

#     # for row in rows:
#     #     print(row)

#     # Step 5: Close the connection
#     # conn.close()

#     return (cursor, conn)