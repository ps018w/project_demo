import cx_Oracle as db
print("Connecting Database....")
connection = db.connect("prem", 'prem123', "localhost:1521/XE")

cursor = connection.cursor()
for row in  cursor.execute("select * from customer where rownum <2"):
    print(row)
cursor.execute("select CUST_NAME from customer")
k=[]
for obj, in cursor:
    k.append(obj)
print(k)