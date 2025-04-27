import psycopg2
import pandas as pd

# 🔗 Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="PhoneBookDB",
    user="postgres",
    password="118523",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# 📌 Create PhoneBook table
cur.execute("""
    CREATE TABLE IF NOT EXISTS PhoneBook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50),
        phone_number VARCHAR(20)
    );
""")
conn.commit()

# 📌 Function to insert data from CSV file
def insert_from_csv(file_pathM):
    df = pd.read_csv(r"C:\Users\sadpo\Documents\demo\Lab10\phonebook.csv")
    print("CSV Data Loaded:", df.head())  # Debugging
    for index, row in df.iterrows():
        cur.execute("INSERT INTO PhoneBook (first_name, phone_number) VALUES (%s, %s)", (row['first_name'], row['phone_number']))
    conn.commit()
    print("CSV Data Inserted Successfully!")

# 📌 Function to insert data from console
def insert_from_console():
    first_name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    cur.execute("INSERT INTO PhoneBook (first_name, phone_number) VALUES (%s, %s)", (first_name, phone_number))
    conn.commit()
    print(f"{first_name} added successfully!")

# 📌 Function to update user data
def update_data():
    update_field = input("Enter field to update (first_name/phone_number): ")
    update_value = input("Enter new value: ")
    user_name = input("Enter user name to update: ")
    cur.execute(f"UPDATE PhoneBook SET {update_field} = %s WHERE first_name = %s", (update_value, user_name))
    conn.commit()
    print(f"{user_name}'s {update_field} updated!")

# 📌 Function to query data with filters
def query_data():
    search_value = input("Enter name or phone to search: ")
    cur.execute("SELECT * FROM PhoneBook WHERE first_name = %s OR phone_number = %s", (search_value, search_value))
    results = cur.fetchall()
    if results:
        print("Results:", results)
    else:
        print("No user found.")

# 📌 Function to delete data from PhoneBook
def delete_data():
    delete_value = input("Enter name or phone to delete: ")
    cur.execute("DELETE FROM PhoneBook WHERE first_name = %s OR phone_number = %s", (delete_value, delete_value))
    conn.commit()
    print(f"{delete_value} deleted successfully!")

# 🔄 Call Functions for Testing
insert_from_csv("C:/Users/sadpo/Documents/demo/Lab10/phonebook.csv")  # Update path if needed
insert_from_console()
query_data()
update_data()
delete_data()

# ✅ Close Connection
cur.close()
conn.close()
print("Database connection closed.")

