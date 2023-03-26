from transaction import Transaction
import pytest

'''
Test each method of the Transaction class. Run using pytest.
'''

trans = Transaction("transactions.db")
trans.clear()

item1 = {'item_no':'1', 'amount':'2', 'category':'fruit', 'date':'2023-03-25', 'desc':'apples'}
item2 = {'item_no':'2', 'amount':'2', 'category':'fruit', 'date':'2021-01-25', 'desc':'pears'}
item3 = {'item_no':'3', 'amount':'2', 'category':'meat', 'date':'2022-02-25', 'desc':'beef'}

def test_show():
    expected = []
    assert trans.show()==expected

def test_add():
    expected = [{'item_no': 1, 'amount': 2, 'category': 'fruit', 'date': '2023-03-25', 'desc': 'apples'}]
    trans.add(item1)
    assert trans.show()==expected    

def test_clear():
    trans.clear()
    expected = []
    assert trans.show()==expected

def test_delete():
    trans.add(item1)
    trans.add(item2)
    trans.delete('2')
    expected = [{'item_no': 1, 'amount': 2, 'category': 'fruit', 'date': '2023-03-25', 'desc': 'apples'}]
    assert trans.show()==expected
'''
def sumbydate():
    expected = ""
    assert trans.show()==expected

def sumbymonth():
    expected = ""
    assert trans.show()==expected

def sumbyyear():
    expected = ""
    assert trans.show()==expected

def sumbycategory():
    expected = ""
    assert trans.show()==expected
'''