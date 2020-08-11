#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states
"""
import MySQLdb
import sys


if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], charset="utf8")

    state = sys.argv[4]
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
    WHERE name LIKE BINARY '{}'".format(state))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
