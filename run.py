import psycopg2
import time
import os

database = os.getenv('DATABASE', 'mathilde')
user = os.getenv('DB_USER', 'mathilde')
password=os.getenv('DB_PWD', '123456')
host=os.getenv('DB_HOST', '127.0.0.1')
port=os.getenv('DB_PORT', '5432')
conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
print "connect success"
cur = conn.cursor()
try:
    cur.execute("CREATE TABLE test(id serial PRIMARY KEY, num integer,data varchar);")
    # #   
    cur.execute("INSERT INTO test(num, data)VALUES(%s, %s)", (1, 'aaa'))
    cur.execute("INSERT INTO test(num, data)VALUES(%s, %s)", (2, 'bbb'))
    cur.execute("INSERT INTO test(num, data)VALUES(%s, %s)", (3, 'ccc'))
except Exception, ex:
    print ex
# cur.execute("CREATE TABLE auto_test(flag integer);")
# cur.execute("INSERT INTO auto_test(flag)VALUES(%s)", '1')
cur.execute("SELECT * FROM test;")
# cur.execute("update auto_test set flag = 0 ;")
conn.commit()
rows = cur.fetchall()        # all rows in table
print(rows)
for i in rows:
    print(i),type(i)
    print i[0], i[1], i[2]
cur.close()
conn.close()

