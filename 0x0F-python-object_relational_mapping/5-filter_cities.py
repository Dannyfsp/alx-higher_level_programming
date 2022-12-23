#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    searched_name = sys.argv[4]
    cur.execute("SELECT c.name \
                FROM cities c \
                JOIN states s \
                ON c.state_id = s.id \
                WHERE BINARY s.name = %s\
                ORDER BY c.id", (searched_name, ))
    query_rows = cur.fetchall()
    cities = []
    for city in query_rows:
        cities.append(city[0])
    print(", ".join(cities))
