"""MySQLdb is an interface for connecting to 
a MySQL database server from Python."""
import MySQLdb
from sys import argv
"""open database communication"""
conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
# prepare a cursor object using cursor() method
cur = conn.cursor()
# execute SQL query using execute() method
query = "SELECT * FROM states ORDER BY id ASC;"
cur.execute(query)
"""# Fetch a rows """
results = cur.fetchall()
for row in results:
    print(row)
    """close both database and cursor"""
cur.close()
conn.close()
