#backend
import sqlite3 as lite

def PatientData():
    con=lite.connect("patient.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS patient(id INTEGER PRIMARY KEY, PntID text, Firstname text, Surname text, DoB text,\
        Age text, Gender text, Address text, MoNo text, LastPersonContact text)")
    con.commit()
    con.close()

def AddPntRec(PntID, Firstname, Surname, DoB, Age, Gender, Address, MoNo, LastPersonContact):
     con=lite.connect("patient.db")
     cur = con.cursor()
     cur.execute("INSERT INTO patient VALUES (NULL,?,?,?,?,?,?,?,?,?)", \
         (PntID, Firstname, Surname, DoB, Age, Gender, Address, MoNo, LastPersonContact))
     con.commit()
     con.close()

def viewData():
    con=lite.connect("patient.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM patient")
    rows = cur.fetchall()
    con.commit()
    con.close()
    return rows

def deleteRec(id):
    con=lite.connect("patient.db")
    cur = con.cursor()
    cur.execute("DELETE FROM patient WHERE id=?", (id,))
    con.commit()
    con.close()

def searchData(PntID="", Firstname="", Surname="", DoB="", Age="", Gender="", Address="",MoNo="", LastPersonContact=""):
    con=lite.connect("patient.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM patient WHERE Pntid=? OR Firstname=? OR Surname=? OR DoB=? OR Age=? OR Gender=? OR Address=? \
        OR MoNo=? OR LastPersonContact=?",(PntID, Firstname, Surname, DoB, Age, Gender, Address, MoNo, LastPersonContact))
    rows=cur.fetchall
    con.commit()
    con.close()

def UpdateData(id, PntID="", Firstname="", Surname="", DoB="", Age="", Gender="", Address="",MoNo="", LastPersonContact=""):
    con=lite.connect("patient.db")
    cur = con.cursor()
    cur.execute("UPDATE patient SET Pntid=?, Firstname=?, Surname=?, DoB=?, Age=?, Gender=?, Address=?, MoNo?, \
        LastPersonContact=?, WHERE id=?",(PntID, Firstname, Surname, DoB, Age, Gender, Address, MoNo, LastPersonContact,id))
    con.commit()
    con.close()

PatientData()
