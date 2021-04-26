#backend
import sqlite3
def PatientData():
    con=sqlite3.connect("patient.db")
    cur.execute("CREATE TABLE IF NOT EXISTS patient(id INTEGER PRIMARY KEY, PntID text, Firstname text, Surname text, DoB text,\
    Age text, Gender text, Address text, Mobile text, LastPersonContact text)")
    con.commit()
    con.clone()

def AddPntRec(PntID, Firstname, Surname, DoB, Age, Gender, Address, Mobile, LastPersonContact):
     con=sqlite3.connect("patient.db")
     cur = con.cursor()
     cur.execute("INSERT INTO patient VALUES(NULL, ?,?,?,?,?,?,?,?,?,)",PntID, Firstname, Surname, DoB, Age, Gender, Address, Mobile, LastPersonContact)
     con.commit()
     con.close()

def viewData():
    con=sqlite3.connect("patient.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM patient")
    row = cur.fetchall()
    con.commit()
    con.close()
    return rows
def deleteRec():
    con=sqlite3.connect("patient.db")
    cur = con.cursor()
    cur.execute("DELETE FROM patient WHERE id=?", (id,))
    con.commit()
    con.close()
def searchData(PntID="", Firstname="", Surname="", DoB="", Age="", Gender="", Address="",Mobile="", LastPersonContact=""):
    con=sqlite3.connect("patient.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM patient WHERE Pntid=? OR Firstname=? OR Surname=? OR DoB=? OR Age=? OR Gender=? OR Address=? \
    OR Mobile=? OR LastPersonContact=?", (PntID, Firstname, Surname, DoB, Age, Gender, Address, Mobile, LastPersonContact,id))
    con.commit()
    con.close()

def UpdateData(id, PntID="", Firstname="", Surname="", DoB="", Age="", Gender="", Address="",Mobile="", LastPersonContact=""):
    con=sqlite3.connect("patient.db")
    cur = con.cursor()
    cur.execute("UPDATE patient Set Pntid=?, Firstname=?, Surname=?, DoB=?, Age=?, Gender=?, Address=?, Mobile=?, \
    LastPersonContact=?, WHERE id=?", (PntID, Firstname, Surname, DoB, Age, Gender, Address, Mobile, LastPersonContact,id))
    con.commit()
    con.close()

PatientData()
