import sqlite3
 
from sqlite3 import Error
 
def sql_connection():
 
    try:
 
        con = sqlite3.connect('City.db')
 
        return con
 
    except Error:
 
        print(Error)
 
def sql_table(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute("CREATE TABLE empoyees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
 
    con.commit()
 
def sql_insert(con, entities):
 
    cursorObj = con.cursor()
 
    cursorObj.execute('INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
 
    con.commit()

def sql_update(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')
 
    con.commit()

def sql_fetch(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute('SELECT id, name FROM employees WHERE salary > 700.0')
 
    rows = cursorObj.fetchall()
 
    for row in rows:
 
        print(row)

def sql_rowcount(con):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM employees')
    rows = cursorObj.fetchall()
    print(len(rows))

def sql_fetchTable(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute('SELECT name from sqlite_master where type= "table"')
 
    print(cursorObj.fetchall())

def sql_fetchCheckTable(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute('create table if not exists projects(id integer, name text)')
    
    con.commit()
	
def sql_fetchDrop(con):
 
    cursorObj = con.cursor()
 
    cursorObj.execute('DROP table if exists employees')
 
    con.commit()

def sql_connectClose(con):
    con.close()

def sql_zadanie(con):
    cursorObj = con.cursor()
    cursorObj.execute('create table if not exists Streets(id integer, nameStreet text, houseNumber integer)')
    data = [(1, "Central", 21), (2, "Youth", 19), (3, "School", 25), (4, "Soviet", 45), (5, "Sadovaya", 2)]
    cursorObj.executemany("INSERT INTO Streets VALUES(?, ?, ?)", data)
    con.commit()

entities = (3, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')

con = sql_connection()
sql_zadanie(con)
sql_connectClose(con)