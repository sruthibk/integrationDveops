# Enter the server name in host
# followed by your user and
# password along with the database 
# name provided by you.
import psycopg2
import pandas as pd

connection = psycopg2.connect(
host = "sruthi-roja-qa1.fyre.ibm.com",
user = "d72e0f9be7e2b11d55576a02",
password = "809bf67ccec54c3e35bce6e9",
database = "postgres"
) 

cursor = connection.cursor()

postgres_insert_query = """ INSERT INTO entries (responsecode, responsemessage) VALUES (%s,%s)"""
record_to_insert = (200, 'OK')
cursor.execute(postgres_insert_query, record_to_insert)

connection.commit()
count = cursor.rowcount
print(count, "Record inserted successfully into  table")




