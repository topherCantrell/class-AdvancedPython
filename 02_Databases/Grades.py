

#import cx_Oracle
#conn = cx_Oracle.connect('pythonhol/welcome@127.0.0.1/orcl')

#import psycopg2
#conn = psycopg2.connect(database='grades', user='dbuser', password='abcd1234', host='192.168.1.4', port='5432', sslmode='require')

import sqlite3

conn = sqlite3.connect("c:/UAH/grades.sqlite")

conn = sqlite3.connect("grades.sqlite")
conn.execute('pragma foreign_keys=ON')

c = conn.cursor()

c.execute('select * from phones')

#first = c.fetchone()
#print(first)

#two = c.fetchmany(2)
#print(two)

phones = c.fetchall()
print(phones)

# POJO (Plain old java object) how to represent data?
# Create a full blown object with get/set? Or just a data dictionary?

# Maybe show a DAO layer and POPOs

phoneRecords = {}
# A list here? why is a dict better?

for e in phones:
    # assumes the columns are in this order. maybe use 'select id,name,phone ...' instead
    rec = {'id':e[0], 'name':e[1], 'phone':e[2]}
    phoneRecords[e[0]] = rec    
    
print(phoneRecords[1])
print(phoneRecords[2])
print(phoneRecords[3])

c.execute('select id,name,grade from grades')
grades = c.fetchall()
print(grades)

gradeRecords = {}
for e in grades:
    rec = {'id':e[0], 'name':e[1], 'grade':e[2]}
    gradeRecords[e[0]] = rec
    
print(gradeRecords[1])

# Print grades
# Print top grade
# Print A's
# Print grades that are primes

# Now repeat but let the DB do the work
# Ah! No DB function to find primes. So must be done be hand.
c.execute('select grades.grade, phones.name from grades,phones where grades.id = phones.id')
rows = c.fetchall()
print(rows)

# Add/change data

# Libraries to ORM python objects

conn.close()

# updates next in trans
