''' transaction.py - a class to make SQL queries to a database of transactions '''

import sqlite3


# written by jack
def to_dict(tpl):
    ''' t is a tuple (item_no,amount,category,date, desc)'''
    todo = {'item_no': tpl[0], 'amount': tpl[1],
            'category': tpl[2], 'date': tpl[3], 'desc': tpl[4]}
    return todo


class Transaction():
    ''' a class to make SQL queries to a database of transactions '''

    # written by jack + kevin
    def __init__(self, dbfile):
        '''Constructor for Transaction. dbfile is file name of the database '''
        self.dbfile = dbfile
        con = sqlite3.connect(dbfile)
        con.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (item_no INT, 
                    amount INT,
                    category VARCHAR(255),
                    date DATE,
                    desc VARCHAR(255))''')
        con.commit()

    # written by kevin
    def show(self):
        ''' return all of the transactions as a list of dicts '''
        return self.run_query("SELECT * from transactions", ())

    # written by kevin + ken
    def add(self, item):
        ''' create a transaction item and add it to the transaction table '''
        return self.run_query("INSERT INTO transactions VALUES(?,?,?,?,?)",
                              (item['item_no'], item['amount'], item['category'],
                               item['date'], item['desc']))

    # written by kevin + ken
    def clear(self):
        ''' delete all of the transactions '''
        return self.run_query("DELETE from transactions", ())

    # written by kevin + ken
    def delete(self, item_no):
        ''' delete a transaction item '''
        return self.run_query("DELETE FROM transactions WHERE item_no=?", (item_no,))

    # written by jack + kevin
    def sort_date(self):
        ''' return transaction(s) sorted by date '''
        return self.run_query('SELECT * from transactions ORDER BY date', ())

    # written by jack
    def summary_date(self, date):
        ''' return transaction(s) from a given date '''
        return self.run_query("SELECT * FROM transactions WHERE strftime('%Y-%m-%d', date)=?",
                              (date,))

    # written by jack
    def summary_month(self, month):
        ''' return transaction(s) from a given month '''
        return self.run_query("SELECT * FROM transactions WHERE strftime('%m', date)=?", (month,))

    # written by jack
    def summary_month_year(self, year_month):
        ''' return transaction(s) from a given month and year '''
        return self.run_query("SELECT * FROM transactions WHERE strftime('%Y-%m', date)=?",
                              (year_month,))

    # written by jack
    def summary_year(self, year):
        ''' return transaction(s) from a given year '''
        return self.run_query("SELECT * FROM transactions WHERE strftime('%Y', date)=?", (year,))

    # written by jack
    def summary_category(self, category):
        ''' return transaction(s) from a given category '''
        return self.run_query("SELECT * from transactions WHERE category=?", (category,))

    # written by kevin
    def run_query(self, query, tpl):
        ''' return all of the transactions as a list of dicts.'''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute(query, tpl)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_dict(t) for t in tuples]
