import mysql.connector as msql
connection = msql.connect(
    host="localhost",        
    user="root",             
    password="root", 
    database="world" 
)
if connection.is_connected():
    print("Connection established with database")
cursor = connection.cursor()
cursor.execute("SHOW TABLES;")
tables = cursor.fetchall()
TName = [] 
num = 1
for i in tables:
    table_name = i[0]
    print(f"{num}. {table_name}")
    TName.append(table_name)
    num += 1
try:
    choice = int(input("\nChoose your table number: ")) 
    if 1 <= choice <= len(TName):
        selected_table = TName[choice - 1]
        
        cursor.execute(f"SELECT * FROM `{selected_table}`")
        data = cursor.fetchall()
        row_num = 1
        print(f"\n--- Data from {selected_table} ---")
        for row in data:
            print(f"{row_num}. {row}")
            row_num += 1
    else:
        print("You chose an invalid table number.")
except ValueError:
    print("Invalid input. Please enter a number.")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("\nDatabase connection closed.")