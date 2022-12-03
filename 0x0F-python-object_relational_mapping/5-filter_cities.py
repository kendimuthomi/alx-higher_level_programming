#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    count = 0
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities
                LEFT JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC""")
    cities = cur.fetchall()
    for city in cities:
        if city[2] == argv[4]:
            if count > 0:
                print(", ", end="")
            print(city[1], end="")
            count = count + 1
    print()
    cur.close()
    db.close()
