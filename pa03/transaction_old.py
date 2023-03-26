import sqlite3
import os


class Transaction:
    def __init__(self, db):
        self.run_query('''CREATE TABLE IF NOT EXISTS transactions
                    (item_no INT, 
                    amount INT,
                    category VARCHAR(50),
                    date DATE,
                    description VARCHAR(50))''',
                       ())

    def select(self, field, value):
        ''' return an item where the field has the given value '''
        return self.run_query("SELECT rowid,* from transactions where (?)=(?)", (field, value))

    def selectAll(self):
        ''' return all of the items as a list of dicts.'''
        return self.run_query("SELECT rowid,* from transactions", ())

    def add(self, item):
        ''' create a transaction item and add it to the transactions table '''
        return self.run_query("INSERT INTO transactions VALUES(?,?,?,?,?)", (item['item_no'], item['amount'], item['category'], item['date'], item['description']))

    def delete(self, rowid):
        ''' delete a transaction item '''
        return self.run_query("DELETE FROM transactions WHERE rowid=(?)", (rowid))

    def run_query(self, query, tuple):
        ''' perform commands on database with sqlite '''
        con = sqlite3.connect(os.getenv('HOME')+'/transactions.db')
        cur = con.cursor()
        cur.execute(query, tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
