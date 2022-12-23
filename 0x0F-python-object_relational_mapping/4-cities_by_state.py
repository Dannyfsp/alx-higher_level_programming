#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()

    cur.execute("SELECT c.id, c.name, s.name \
                FROM cities c \
                JOIN states s \
                ON c.state_id = s.id \
                ORDER BY c.id")
    query_rows = cur.fetchall()

    for city in query_rows:
        print(city)
