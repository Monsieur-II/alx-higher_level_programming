#!/usr/bin/python3
"""
 takes in the name of a state as an arg and lists all cities of that state
 using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    match = sys.argv[4]
    cur.execute("""SELECT cities.name FROM cities JOIN states
    ON cities.state_id = states.id WHERE states.name = %s
    ORDER BY cities.id""", (match,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
