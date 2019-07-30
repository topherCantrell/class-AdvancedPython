
import sqlite3

def printCustomer(row):
    print(row[0]+" has "+str(row[1])+" cats and "+str(row[2])+" dogs.")
    
def printCustomers():
    conn = sqlite3.connect("pets.sqlite")
    try:
        c = conn.cursor()
        c.execute("select name, cats, dogs from pets")
        rows = c.fetchall()
        for r in rows:
            printCustomer(r)
    finally:
        conn.close()
    
def printBenjiWinners(): # 1 dog and 0 cats
    print("Benji Winners:")
    conn = sqlite3.connect("pets.sqlite")
    try:
        c = conn.cursor()
        c.execute("select name, cats, dogs from pets where dogs=1 and cats=0")
        rows = c.fetchall()
        for r in rows:
            printCustomer(r)
    finally:
        conn.close()

def printOneWayWinners(): # One type of pet
    print("One-Way Winners:")
    conn = sqlite3.connect("pets.sqlite")
    try:
        c = conn.cursor()
        c.execute("select name, cats, dogs from pets where (dogs=0 or cats=0) and (dogs>0 or cats>0)")
        rows = c.fetchall()
        for r in rows:
            printCustomer(r)
    finally:
        conn.close()

def printCatLadyWinners(): # More than 6 cats
    print("Cat-Lady Winners:")
    conn = sqlite3.connect("pets.sqlite")
    try:
        c = conn.cursor()
        c.execute("select name, cats, dogs from pets where cats>6")
        rows = c.fetchall()
        for r in rows:
            printCustomer(r)
    finally:
        conn.close()

def printZooKeeperWinners(): # More than 10 pets
    print("Zoo-Keeper Winners:")
    conn = sqlite3.connect("pets.sqlite")
    try:
        c = conn.cursor()
        c.execute("select name, cats, dogs from pets where (cats + dogs > 10)")
        rows = c.fetchall()
        for r in rows:
            printCustomer(r)
    finally:
        conn.close()
