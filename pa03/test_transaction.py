from transaction import Transaction
import pytest

'''
Test each method of the Transaction class. Run using pytest.
'''

trans = Transaction("transactions.db")
trans.clear()

item1 = {'item_no': '1', 'amount': '2', 'category': 'fruit',
         'date': '2023-03-25', 'desc': 'apples'}
item2 = {'item_no': '2', 'amount': '2', 'category': 'fruit',
         'date': '2021-01-25', 'desc': 'pears'}
item3 = {'item_no': '3', 'amount': '2', 'category': 'meat',
         'date': '2022-02-25', 'desc': 'beef'}


def test_show():
    trans.clear()
    expected = []
    assert trans.show() == expected


def test_add():
    trans.clear()
    expected = [{'item_no': 1, 'amount': 2, 'category': 'fruit',
                 'date': '2023-03-25', 'desc': 'apples'}]
    trans.add(item1)
    assert trans.show() == expected


def test_clear():
    trans.clear()
    trans.add(item1)
    trans.clear()
    expected = []
    assert trans.show() == expected


def test_delete():
    trans.clear()
    trans.add(item1)
    trans.add(item2)
    trans.delete(2)
    expected = [{'item_no': 1, 'amount': 2, 'category': 'fruit',
                 'date': '2023-03-25', 'desc': 'apples'}]
    assert trans.show() == expected


def test_sort_date():
    trans.clear()
    trans.add(item1)
    trans.add(item2)
    trans.add(item3)
    expected = [{'item_no': 2, 'amount': 2, 'category': 'fruit',
                'date': '2021-01-25', 'desc': 'pears'},
                {'item_no': 3, 'amount': 2, 'category': 'meat',
                'date': '2022-02-25', 'desc': 'beef'},
                {'item_no': 1, 'amount': 2, 'category': 'fruit',
                'date': '2023-03-25', 'desc': 'apples'}]
    assert trans.sort_date() == expected


def test_summary_date():
    trans.clear()
    trans.add(item1)
    trans.add(item2)
    trans.add(item3)
    expected = [{'item_no': 3, 'amount': 2, 'category': 'meat',
                'date': '2022-02-25', 'desc': 'beef'}]
    assert trans.summary_date('2022-02-25') == expected


def test_summary_month():
    trans.clear()
    trans.add(item1)
    trans.add(item2)
    trans.add(item3)
    expected = [{'item_no': 2, 'amount': 2, 'category': 'fruit',
                'date': '2021-01-25', 'desc': 'pears'}]
    assert trans.summary_month('01') == expected


def test_summary_month_year():
    trans.clear()
    trans.add(item1)
    trans.add(item2)
    trans.add(item3)
    expected = [{'item_no': 2, 'amount': 2, 'category': 'fruit',
                'date': '2021-01-25', 'desc': 'pears'}]
    assert trans.summary_month_year('2021-01') == expected


def test_summary_year():
    trans.clear()
    trans.add(item1)
    trans.add(item2)
    trans.add(item3)
    expected = [{'item_no': 1, 'amount': 2, 'category': 'fruit',
                'date': '2023-03-25', 'desc': 'apples'}]
    assert trans.summary_year('2023') == expected


def test_summary_category():
    trans.clear()
    trans.add(item1)
    trans.add(item2)
    trans.add(item3)
    expected = [{'item_no': 1, 'amount': 2, 'category': 'fruit',
                'date': '2023-03-25', 'desc': 'apples'},
                {'item_no': 2, 'amount': 2, 'category': 'fruit',
                'date': '2021-01-25', 'desc': 'pears'}]
    assert trans.summary_category('fruit') == expected
