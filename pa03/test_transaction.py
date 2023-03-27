''' Test each method of the Transaction class. Run using pytest. '''

from transactions import Transaction

trans = Transaction("transactions.db")
trans.clear()

item1 = {'item_no': '1', 'amount': '2', 'category': 'fruit',
         'date': '2023-03-25', 'desc': 'apples'}
item2 = {'item_no': '2', 'amount': '2', 'category': 'fruit',
         'date': '2021-01-25', 'desc': 'pears'}
item3 = {'item_no': '3', 'amount': '2', 'category': 'meat',
         'date': '2022-02-25', 'desc': 'beef'}


def test_show():
    ''' Test show method '''
    trans.clear()
    expected = []
    assert trans.show() == expected


def test_add():
    ''' Test add method '''
    trans.clear()
    expected = [{'item_no': 1, 'amount': 2, 'category': 'fruit',
                 'date': '2023-03-25', 'desc': 'apples'}]
    trans.add(item1)
    assert trans.show() == expected


def test_clear():
    ''' Test clear method '''
    trans.clear()
    trans.add(item1)
    trans.clear()
    expected = []
    assert trans.show() == expected


def test_delete():
    ''' Test delete method '''
    trans.clear()
    trans.add(item1)
    trans.add(item2)
    trans.delete(2)
    expected = [{'item_no': 1, 'amount': 2, 'category': 'fruit',
                 'date': '2023-03-25', 'desc': 'apples'}]
    assert trans.show() == expected


def test_sort_date():
    ''' Test sort_date method '''
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
    ''' Test summary_date method '''
    trans.clear()
    trans.add(item1)
    trans.add(item2)
    trans.add(item3)
    expected = [{'item_no': 3, 'amount': 2, 'category': 'meat',
                'date': '2022-02-25', 'desc': 'beef'}]
    assert trans.summary_date('2022-02-25') == expected


def test_summary_month():
    ''' Test summary_month method '''
    trans.clear()
    trans.add(item1)
    trans.add(item2)
    trans.add(item3)
    expected = [{'item_no': 2, 'amount': 2, 'category': 'fruit',
                'date': '2021-01-25', 'desc': 'pears'}]
    assert trans.summary_month('01') == expected


def test_summary_month_year():
    ''' Test summary_month_year method '''
    trans.clear()
    trans.add(item1)
    trans.add(item2)
    trans.add(item3)
    expected = [{'item_no': 2, 'amount': 2, 'category': 'fruit',
                'date': '2021-01-25', 'desc': 'pears'}]
    assert trans.summary_month_year('2021-01') == expected


def test_summary_year():
    ''' Test summary_year method '''
    trans.clear()
    trans.add(item1)
    trans.add(item2)
    trans.add(item3)
    expected = [{'item_no': 1, 'amount': 2, 'category': 'fruit',
                'date': '2023-03-25', 'desc': 'apples'}]
    assert trans.summary_year('2023') == expected


def test_summary_category():
    ''' Test summary_category method '''
    trans.clear()
    trans.add(item1)
    trans.add(item2)
    trans.add(item3)
    expected = [{'item_no': 1, 'amount': 2, 'category': 'fruit',
                'date': '2023-03-25', 'desc': 'apples'},
                {'item_no': 2, 'amount': 2, 'category': 'fruit',
                'date': '2021-01-25', 'desc': 'pears'}]
    assert trans.summary_category('fruit') == expected
