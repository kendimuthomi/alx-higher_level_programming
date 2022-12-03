#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities
                LEFT JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC""")
    cities = cur.fetchall()
    for city in cities:
        print(city)
    cur.close()
    db.close()
