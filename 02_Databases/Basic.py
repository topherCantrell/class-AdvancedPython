import sqlite3

class StudentRecord:
    
    def __init__(self, uid, name, phone):
        self.uid = uid
        self.name = name
        self.phone = phone
    
    def getUID(self):
        return self.uid
    
    def getName(self):
        return self.name
    
    def getPhone(self):
        return self.phone
    
    def __repr__(self):
        return 'id='+str(self.uid)+\
            ' name='+self.name+\
            ' phone='+self.phone

#conn = sqlite3.connect("c:/UAH/grades.sqlite")
conn = sqlite3.connect("grades.sqlite")
conn.execute('pragma foreign_keys=ON')

c = conn.cursor()
c.execute('select id,name,phone from students')
studentsRows = c.fetchall()
c.execute('select name,grade from grades')
gradesRows = c.fetchall()

print(studentsRows)
print(gradesRows)

chris = studentsRows[0]
print(chris[2])
#chris[2] = '777'

#

students = {}
for p in studentsRows:
    rec = {'uid':p[0], 'name':p[1], 'phone':p[2]}
    students[p[0]] = rec

print(students)
    
chris = students[20]
print(chris)

chris['phone'] = '777'
print(chris)

students = {}
for p in studentsRows:
    rec = StudentRecord(p[0],p[1],p[2])
    students[p[0]] = rec
    
print(students)
    
print(students[20].getName())

#students[20].setUID(55)

students = {}
for p in studentsRows:
    rec = {'uid':p[0], 'name':p[1], 'phone':p[2]}
    students[p[0]] = rec
    
grades = []
for g in gradesRows:
    rec = {'student':g[0], 'grade':g[1]}
    grades.append(rec)

print(grades)

def printHighestGrade():
    high = grades[0]
    for g in grades:
        if g['grade'] > high['grade']:
            high = g
    #print g
    
    st = students[high['student']]
    print(str(high['grade'])+" "+st['name'])
    
printHighestGrade()

conn.close()


def printHighestGrade2():
    conn = sqlite3.connect("grades.sqlite")
    c = conn.cursor()

    c.execute("""select 
        students.name, grades.grade 
        from 
        students,grades where 
        students.id=grades.name order 
        by grades.grade desc""")
    recs = c.fetchone()

    print(str(recs[1])+" "+recs[0])

    conn.close()
    
print("HERE")
printHighestGrade2()




# Wait ... what if there are multiples with the same high grade?        
