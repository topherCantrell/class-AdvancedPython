import sqlite3

def printGrades():
    conn = sqlite3.connect("grades.sqlite")
    c = conn.cursor()
    c.execute('select grades.grade, students.id, students.name from students,grades where students.id=grades.student')
    gradesRows = c.fetchall()
    print(gradesRows)
    conn.close()
    
