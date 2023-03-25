import sqlite3
import os


def toDict(t):
    ''' t is a tuple (rowid,title, desc,completed)'''
    print('t='+str(t))
    todo = {'item_no':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'desc' : t[4]}
    return todo

class Transaction():
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                    (item_no INT, 
                    amount INT,
                    category VARCHAR(255),
                    date DATE,
                    desc VARCHAR(255))''',
                    ())
    
    def selectActive(self):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        return self.runQuery("SELECT rowid,* from todo where completed=0",())

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

    def setComplete(self,rowid):
        ''' mark a todo item as completed '''
        return self.runQuery("UPDATE todo SET completed=1 WHERE rowid=(?)",(rowid,))

    def runQuery(self,query,tuple):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con= sqlite3.connect('transaction.db')
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]