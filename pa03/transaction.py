''' transaction.py - a class to make SQL queries to a database of transactions '''

import sqlite3


def to_dict(tpl):
    ''' t is a tuple (rowid,title, desc,completed)'''
    todo = {'item_no': tpl[0], 'amount': tpl[1],
            'category': tpl[2], 'date': tpl[3], 'desc': tpl[4]}
    return todo


class Transaction():
    ''' a class to make SQL queries to a database of transactions '''

    def __init__(self, dbfile):
        con = sqlite3.connect(dbfile)
        con.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (item_no INT, 
                    amount INT,
                    category VARCHAR(255),
                    date DATE,
                    desc VARCHAR(255))''')
        con.commit()
        self.run_query('''CREATE TABLE IF NOT EXISTS transactions
                    (item_no INT, 
                    amount INT,
                    category VARCHAR(255),
                    date DATE,
                    desc VARCHAR(255))''',
                       ())

    def show(self):
        ''' return all of the transaction as a list of dicts '''
        return self.run_query("SELECT * from transactions", ())

    def add(self, item):
        ''' create a transaction item and add it to the todo table '''
        return self.run_query("INSERT INTO transactions VALUES(?,?,?,?,?)",
                              (item['item_no'], item['amount'], item['category'],
                               item['date'], item['desc']))

    def clear(self):
        ''' delete all of the transaction '''
        return self.run_query("DELETE from transactions", ())

    def delete(self, item_no):
        ''' delete a transaction item '''
        return self.run_query("DELETE FROM transactions WHERE item_no=(?)", (item_no,))

    def sumbydate(self):
        ''' return transaction sorted by date '''
        return self.run_query('SELECT * from transactions ORDER BY date', ())

    def sumbymonth(self):
        ''' return transaction sorted by month '''
        # not working
        return self.run_query("SELECT * FROM transactions GROUP BY FORMAT (date, 'MM')", ())

    def sumbyyear(self):
        ''' return transaction sorted by year '''
        # working, but not correctly
        return self.run_query('SELECT * from transactions ORDER BY date', ())

    def sumbycategory(self, category):
        ''' return transaction sorted by category '''
        return self.run_query("SELECT * from transactions WHERE category=?", (category,))

    def run_query(self, query, tpl):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con = sqlite3.connect('transactions.db')
        cur = con.cursor()
        cur.execute(query, tpl)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_dict(t) for t in tuples]
