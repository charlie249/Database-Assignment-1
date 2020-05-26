import sqlite3
db = sqlite3.connect('/Users/charlie/Documents/Git/Database-Assignment-1/Assignment _1_Database.db')
cursor = db.cursor()
shopper_id = input("Enter a shopper_id: ")
print("ORINOCO - SHOPPER MAIN MENU")
print("•    Display your order history")
print("•    Add an item to your basket")
print("•    View your basket")
print("•    Checkout")
print("•    Exit")

sql_query = "SELECT order_id, order_date \
		   FROM shopper_orders \
           ORDER BY order_date DESC"
cursor.execute(sql_query)
all_sell_rows = cursor.fetchall()
if all_sell_rows:
    
else:
    print("No seller found")
db.close()