# issue_001

# runnning steps ... 

# - step 1 
## - create posgress database 
### ( CREATE DATABASE smartcarv0; ) 
### (CREATE USER smartcaruser WITH PASSWORD 'smartcarpassword';) 
### ( GRANT ALL PRIVILEGES ON DATABASE "smartcarv0" to smartcaruser; )



# - step 2
## -  docker build -t tag66 .

## - docker run tag66

you should recive  : 
could not connect to server: Connection refused
        Is the server running on host "127.0.0.1" and accepting
        TCP/IP connections on port 5432?

reconnect: 5
start psycopg2.connect  ....  
could not connect to server: Connection refused
        Is the server running on host "127.0.0.1" and accepting
        TCP/IP connections on port 5432?

reconnect: 4
start psycopg2.connect  ....  
could not connect to server: Connection refused
        Is the server running on host "127.0.0.1" and accepting
        TCP/IP connections on port 5432?

reconnect: 3
start psycopg2.connect  ....  
could not connect to server: Connection refused
        Is the server running on host "127.0.0.1" and accepting
        TCP/IP connections on port 5432?

reconnect: 2
start psycopg2.connect  ....  
could not connect to server: Connection refused
        Is the server running on host "127.0.0.1" and accepting
        TCP/IP connections on port 5432?

reconnect: 1