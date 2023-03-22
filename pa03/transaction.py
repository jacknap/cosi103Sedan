class Transaction:
    def __init__(self, db):
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions
                    (item_no INT, 
                    amount INT,
                    category VARCHAR(50),
                    date DATE,
                    description VARCHAR(50))''',
                    ())
        
    def select(self, field, value):
        ''' return an item where the field has the given value '''
        return self.runQuery("SELECT rowid,* from transactions where (?)=(?)",(field, value))

    def selectAll(self):
        ''' return all of the items as a list of dicts.'''
        return self.runQuery("SELECT rowid,* from transactions",())

    def add(self, item):
        ''' create a transaction item and add it to the transactions table '''
        return self.runQuery("INSERT INTO transactions VALUES(?,?,?,?,?)",(item['item_no'],item['amount'],item['category'],item['date'],item['description']))

    def delete(self,rowid):
        ''' delete a transaction item '''
        return self.runQuery("DELETE FROM transactions WHERE rowid=(?)",(rowid))

    def runQuery(self,query,tuple):
        ''' perform commands on database with sqlite '''
        con= sqlite3.connect(os.getenv('HOME')+'/transactions.db')
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        