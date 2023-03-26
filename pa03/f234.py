import sqlite3


def toDict(t):
    ''' t is a tuple (rowid,title, desc,completed)'''
    # print('t='+str(t))
    todo = {'item_no': t[0], 'amount': t[1],
            'category': t[2], 'date': t[3], 'desc': t[4]}
    return todo


class Transaction():
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
        return self.run_query("INSERT INTO transactions VALUES(?,?,?,?,?)", (item['item_no'], item['amount'], item['category'], item['date'], item['desc']))

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
        #print(self.run_query("SELECT FORMAT(date, 'MM') as date",()))
        return self.run_query("SELECT * FROM transactions GROUP BY FORMAT (date, 'MM')", ())

    def sumbyyear(self):
        ''' return transaction sorted by year '''
        return self.run_query('SELECT * from transactions ORDER BY date', ())

    def run_query(self, query, tpl):
        ''' return all of the uncompleted tasks as a list of dicts.'''
        con = sqlite3.connect('transaction.db')
        cur = con.cursor()
        cur.execute(query, tpl)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]
