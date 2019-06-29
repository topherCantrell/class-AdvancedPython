import sqlite3

import DBUtil

DBUtil.printGrades()

conn = sqlite3.connect("grades.sqlite")

c = conn.cursor()

c.execute('update grades set grade=90 where student=17')
c.execute('update grades set grade=92 where student=35')

conn.commit()

#c.execute('select grade,student from grades')
#gradesRows = c.fetchall()
#print(gradesRows)

conn.close()

DBUtil.printGrades()

conn = sqlite3.connect("grades.sqlite")

try:        

    c = conn.cursor()

    c.execute('update grades set grade=90 where name=17')

    # what if error happens here? Moving money between accounts? database crashes
    empty = []
    empty[5] = 0

    c.execute('update grades set grade=92 where name=35')
    
    conn.commit()
    
except:
    
    print("BAD")
    conn.rollback()

finally:
    conn.close()



with sqlite3.connect("grades.sqlite") as conn2:
    
    c = conn2.cursor()
    c.execute('update grades set grade=90 where student=17')
    c.execute('update grades set grade=92 where student=35')
        
    conn2.commit()
    
conn2.close()

c = conn2.cursor()

c.execute('select * from grades')
print(c.fetchall())
