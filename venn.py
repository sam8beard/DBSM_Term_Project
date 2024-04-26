import sqlite3

# Step 1: Read the CSV file into a DataFrame
import pandas as pd
df = pd.read_csv('athlete_events.csv')

# Step 2: Connect to the SQLite database and create it if it doesn't exist
conn = sqlite3.connect('your_database.db')

# Step 3: Write DataFrame to the database
df.to_sql('table_name', conn, if_exists='replace', index=False)

# Step 4: Perform queries
cursor = conn.cursor()
# cursor.execute("SELECT * FROM table_name WHERE condition")
cursor.execute("SELECT * FROM table_name")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Step 5: Close the connection
conn.close()
