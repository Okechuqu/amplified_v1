import sqlite3
import os
from decouple import config
# Connect to the database (if it doesn't exist, it will be created)


def databaseWebsiteStorageDB(name='',  path=''):
    _database = os.path.abspath('website.db')
    conn = sqlite3.connect(_database)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    tablename = 'website'
    # Create a table (if it doesn't exist)
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {tablename}
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL, path TEXT NOT NULL)''')

    # Check if the data already exists in the table
    cursor.execute(f"SELECT COUNT(*) FROM {tablename}")
    result = cursor.fetchone()[0]

    # Insert or update data in the table
    if result == 0:
        cursor.execute(
            f"INSERT INTO {tablename} (name, path) VALUES (?,?)", (name, path,))
        conn.commit()
        print("Data inserted successfully.")
    else:
        cursor.execute(
            f"UPDATE {tablename} SET name=?, path=?  WHERE id=1", (name, path,))
        conn.commit()
        print("Data updated successfully.")

    # Close the cursor and connection
    cursor.close()
    conn.close()

# Test the function
# databaseWebsiteStorageDB(name="Example 34567", path="loadsd......" )


def sqliteGet():
    _database = os.path.abspath('website.db')
    conn = sqlite3.connect(_database)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    tablename = 'website'
    data = {}

    # Alter the table to add the "path" column
    # cursor.execute("ALTER TABLE website ADD COLUMN path TEXT")

    # Execute a SELECT query to check if there is any data in the table
    cursor.execute(f"SELECT * FROM {tablename}")

    # Retrieve the result
    result = cursor.fetchall()

    # Check if there is any data
    if len(result) > 0:
        data['name'] = result[0][1]
        data['path'] = result[0][2]
        data['app'] = f"{config('WEBSITE_DIR')}.{result[0][1]}"
    else:
        data = None

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Check if data is None or a dictionary
    if data is not None:
        # Return the selected app and URL file
        return [data.get('app')], f"{data.get('app')}.urls" #, f"{data.get('path')}"
    else:
        # Handle the case when there is no data
        return [], None


