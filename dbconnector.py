import mysql.connector
from utilities.config  import *

from cryptography.fernet import Fernet
#conn= mysql.connector.connect(host="3.6.151.159",database="koilhardwar_beta",user="atpl-remote",password="Atpl@123")
conn=getConnection()
print(conn.is_connected())
cursor = conn.cursor()
# cursor.execute("SHOW TABLES")
# table_list = cursor.fetchall()
# for table in table_list:
#     print(table)
table_name = 'app_users'
#
# # Execute a query to fetch the table's metadata
# #table_name = 'your_table_name'
query = f"DESCRIBE {table_name}"
cursor.execute(query)
# # Fetch all the rows returned by the query
rows = cursor.fetchall()
#
# # Extract the field names from the rows
#field_names = [row[1] for row in rows]
#
# # Print the field names
for field_name in rows:
    print(field_name[0])

# Close the database connection
#conn.close()

#print(first_user[1])
#print(first_user[1][1])
cursor.execute("Select * from app_users")
user_list = cursor.fetchall()
for user in user_list:
    print(user)

update_query="update app_users set firm = %s where owner_name = %s"
data_update=("Pooja","Pooja Traders")
cursor.execute(update_query,data_update)
conn.commit()
cursor.close()
conn.close()