#!/usr/bin/python3
"""
This script lists all states, that start with 'N',
from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id")
    query_rows = cur.fetchall()

    for state in query_rows:
        if state[1][0] == 'N':
            print(state)
# cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
