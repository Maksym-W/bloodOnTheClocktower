import sqlite3

# Connect to the database file (it will create the file if it does not exist)
conn = sqlite3.connect('game.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS roles
                  (role_name TEXT PRIMARY KEY, role_description TEXT, town_allegiance TEXT)''')

# Insert some data
cursor.execute("INSERT INTO roles (role_name, role_description, town_allegiance) VALUES ('Sheriff', 'Maintains the order', 'Town')")
cursor.execute("INSERT INTO roles (role_name, role_description, town_allegiance) VALUES ('Doctor', 'Heals the wounded', 'Town')")
cursor.execute("INSERT INTO roles (role_name, role_description, town_allegiance) VALUES ('Mafioso', 'Works in the shadows', 'Mafia')")

# Commit the changes
conn.commit()

# Close the connection
conn.close()
