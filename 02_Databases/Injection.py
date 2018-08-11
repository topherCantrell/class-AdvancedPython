
import sqlite3

#conn = sqlite3.connect("c:/UAH/grades.sqlite")

conn = sqlite3.connect("grades.sqlite")
conn.execute('pragma foreign_keys=ON')

c = conn.cursor()

"""
c.execute("select * from users")
phones = c.fetchall()
print(phones)

c.execute("select * from users where name='Chris' and pass='topher'")
users = c.fetchall()
print(users[0])
"""

name = 'Chris'
password = 'topher'

c.execute("select * from users where name='"+name+"' and pass='"+password+"'")
user = c.fetchone()
print(user)


name = 'Chris'
password = "' or ''='' --"

c.execute("select * from users where name='"+name+"' and pass='"+password+"'")
user = c.fetchone()
print(user)


name = 'Chris'
password = 'topher'

c.execute("select * from users where name=? and pass=?",(name,password))
users = c.fetchall()
print(users[0])

name = 'Chris'
password = "' or ''='' --"

# fetchone

c.execute("select * from users where name=? and pass=?",(name,password))
user = c.fetchone()
print(user)

c.execute("select * from users where name=?",name)

print(sqlite3.paramstyle)

conn.close()

