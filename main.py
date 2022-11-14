import psycopg2
import os
import time
 


print("DB_NAME" , os.environ['DB_NAME'])
print("DB_USER" , os.environ['DB_USER'])
print("DB_PASSWORD" , os.environ['DB_PASSWORD'])
print("DB_HOST" , os.environ['DB_HOST'])
print("DB_PORT" , os.environ['DB_PORT'])
 
print()
print()
print("start psycopg2.connect  ....  ")
reconnect = 5
conn = None
 
while True:
    try:
        print("start psycopg2.connect  ....  ")
        conn = psycopg2.connect(
            dbname= os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
            host=os.environ["DB_HOST"],
            port=os.environ["DB_PORT"],
        )
        print(" psycopg2.connect pass :) ")
        break
    except Exception as e:
        print(e)
        print(f"reconnect: {reconnect}")
        time.sleep(1)
        reconnect -= 1
        if reconnect == 0:
            break
         
print("start psycopg2.connect  done :)  ")
print()
print()
print()