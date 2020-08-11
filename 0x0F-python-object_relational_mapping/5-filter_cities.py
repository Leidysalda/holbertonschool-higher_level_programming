#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf8")

    state = (sys.argv[4])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
    FROM cities INNER JOIN states\
    ON cities.state_id = states.id\
    WHERE states.name = '%state'")
    rows = cur.fetchall()
    for i in range(len(rows)):
        print(rows[i][0], end="")
        if i != len(rows) - 1:
            print(", ", end="")
    print("")
    cur.close()
    db.close()
