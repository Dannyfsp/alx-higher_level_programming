#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    searched_name = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE BINARY name = %s ORDER BY id",
                (searched_name, ))
    query_rows = cur.fetchall()

    for state in query_rows:
        print(state)
