import sqlite3
import os


def toDict(t):
    ''' t is a tuple (rowid,title, desc,completed)'''
    #print('t='+str(t))
    todo = {'item_no':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'desc' : t[4]}
    return todo

class Transaction():
    def __init__(self, dbfile):
        con = sqlite3.connect(dbfile)
        cur = con.cursor()
        con.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (item_no INT, 
                    amount INT,
                    category VARCHAR(255),
                    date DATE,
                    desc VARCHAR(255))''')
        con.commit()
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                    (item_no INT, 
                    amount INT,
                    category VARCHAR(255),
                    date DATE,
                    desc VARCHAR(255))''',
                    ())
    

    def show(self):
        ''' return all of the tasks as a list of dicts.'''
        return self.runQuery("SELECT * from transactions",())

    def add(self,item):
        ''' create a todo item and add it to the todo table '''
        
        return self.runQuery("INSERT INTO transactions VALUES(?,?,?,?,?)",(item['item_no'],item['amount'],item['category'],item['date'],item['desc']))

    def clear(self):
        return self.runQuery("DELETE from transactions",())
       

    def delete(self,item_no):
        ''' delete a todo item '''
        return self.runQuery("DELETE FROM transactions WHERE item_no=(?)",(item_no,))

    def sumbydate(self):
        return self.runQuery('SELECT * from transactions ORDER BY date', ())
    
    def sumbymonth(self):
        #print(self.runQuery("SELECT FORMAT(date, 'MM') as date",()))
        return self.runQuery("SELECT * FROM transactions GROUP BY FORMAT (date, 'MM')", ())
    
    def sumbyyear(self):
        return self.runQuery('SELECT * from transactions ORDER BY date', ())

    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect('transaction.db')
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]