import mysql.connector
try:
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        port=3306
    )
    print("Connected successfully")
    conn.close()
except Exception as e:
    print(f"Failed: {e}")
