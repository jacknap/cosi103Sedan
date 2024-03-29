# PA03 Finance Tracker

Application for tracking transactions utilizing an SQL database.

Features:

- add transactions
- delete transactions
- summarize transactions by date and category

## pylint

```
cosi103Sedan\pa03> pylint .\transactions.py

---

Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

cosi103Sedan\pa03> pylint .\tracker.py
**\*\***\***\*\*** Module tracker
tracker.py:41:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:53:0: R0912: Too many branches (28/12) (too-many-branches)
tracker.py:53:0: R0915: Too many statements (58/50) (too-many-statements)

---

Your code has been rated at 9.49/10 (previous run: 9.49/10, +0.00)

cosi103Sedan\pa03> pylint .\test_transaction.py

---

Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

## pytest

```
cosi103Sedan\pa03> pytest
=================================================================== test session starts ===================================================================
platform win32 -- Python 3.9.16, pytest-7.1.2, pluggy-1.0.0
rootdir: C:\Users\jackn\Documents\Work\Software Engineering\Code\cosi103Sedan\pa03
plugins: anyio-3.5.0
collected 10 items

test_transaction.py .......... [100%]

=================================================================== 10 passed in 0.69s ====================================================================
```


## tracker.py Demo

```
cosi103Sedan\pa03> python tracker.py
Enter a number to execute that command:
            0. quit
            1. show transactions
            2. add transaction
                Usage: "2 item_no amount category YYYY-MM-DD description"
            3. delete transaction
                Usage: "3 item_no"
            4. delete all transactions
            5. summarize transactions by date
                Usage: "5 YYYY-MM-DD" for items from the given date
                    or "5" for all items sorted by date
            6. summarize transactions by month
                Usage: "6 MM"
                    or "6 YYYY-MM"
            7. summarize transactions by year
                Usage: "7 YYYY"
            8. summarize transactions by category
                Usage: "8 category"
            9. print this menu

> 1

item #     amount     category   date            description
------------------------------------------------------------
item_no    amount     category   date            description
item_no    amount     category   date            description
2021-03-04 5          4000       groceries       apples
------------------------------------------------------------

> 4
Are you sure you want to delete all transactions? (y/n)
> y
------------------------------------------------------------

> 2
Incorrect syntax
Usage: "2 item_no amount category YYYY-MM-DD description"

------------------------------------------------------------

> 1
no transactions to print
------------------------------------------------------------

> 2 13 450 apples 2023-01-02 food
------------------------------------------------------------

> 2 15 550 bananas 2023-03-02 morefood
------------------------------------------------------------

> 1

item #     amount     category   date            description
------------------------------------------------------------
13         450        apples     2023-01-02      food
15         550        bananas    2023-03-02      morefood
------------------------------------------------------------

> 2 23 450 grapes 2023-03-22 snacks 
------------------------------------------------------------

> 2 10 200 pears 2020-02-01 gift
------------------------------------------------------------

> 2 20 56 apricot 2018-05-23 date
------------------------------------------------------------

> 1

item #     amount     category   date            description
------------------------------------------------------------
13         450        apples     2023-01-02      food
15         550        bananas    2023-03-02      morefood
23         450        grapes     2023-03-22      snacks
10         200        pears      2020-02-01      gift
20         56         apricot    2018-05-23      date
------------------------------------------------------------

> 5
Transactions sorted by date:

item #     amount     category   date            description
------------------------------------------------------------
20         56         apricot    2018-05-23      date
10         200        pears      2020-02-01      gift
13         450        apples     2023-01-02      food
15         550        bananas    2023-03-02      morefood
23         450        grapes     2023-03-22      snacks
------------------------------------------------------------

> 6 02
Transactions from month 02:

item #     amount     category   date            description
------------------------------------------------------------
10         200        pears      2020-02-01      gift
------------------------------------------------------------

> 6 03
Transactions from month 03:

item #     amount     category   date            description
------------------------------------------------------------
15         550        bananas    2023-03-02      morefood
23         450        grapes     2023-03-22      snacks
------------------------------------------------------------

> 6 12 
Transactions from month 12:
no transactions to print
------------------------------------------------------------

> 7 2021
Transactions from 2021:
no transactions to print
------------------------------------------------------------

> 7 2023
Transactions from 2023:

item #     amount     category   date            description
------------------------------------------------------------
13         450        apples     2023-01-02      food
15         550        bananas    2023-03-02      morefood
23         450        grapes     2023-03-22      snacks
------------------------------------------------------------

> 7 2018
Transactions from 2018:

item #     amount     category   date            description
------------------------------------------------------------
20         56         apricot    2018-05-23      date
------------------------------------------------------------

> 8 apples
Transactions from the apples category:

item #     amount     category   date            description
------------------------------------------------------------
13         450        apples     2023-01-02      food
------------------------------------------------------------

> 2 14 230 apples 2019-06-13 for_sophia
------------------------------------------------------------

> 8 apples
Transactions from the apples category:

item #     amount     category   date            description
------------------------------------------------------------
13         450        apples     2023-01-02      food
14         230        apples     2019-06-13      for_sophia
------------------------------------------------------------

> 9 
Enter a number to execute that command:
            0. quit
            1. show transactions
            2. add transaction
                Usage: "2 item_no amount category YYYY-MM-DD description"
            3. delete transaction
                Usage: "3 item_no"
            4. delete all transactions
            5. summarize transactions by date
                Usage: "5 YYYY-MM-DD" for items from the given date
                    or "5" for all items sorted by date
            6. summarize transactions by month
                Usage: "6 MM"
                    or "6 YYYY-MM"
            7. summarize transactions by year
                Usage: "7 YYYY"
            8. summarize transactions by category
                Usage: "8 category"
            9. print this menu

------------------------------------------------------------

> 4 
Are you sure you want to delete all transactions? (y/n)
> n
Did not delete all transactions

------------------------------------------------------------

> 1

item #     amount     category   date            description
------------------------------------------------------------
13         450        apples     2023-01-02      food
15         550        bananas    2023-03-02      morefood
23         450        grapes     2023-03-22      snacks
10         200        pears      2020-02-01      gift
20         56         apricot    2018-05-23      date
14         230        apples     2019-06-13      for_sophia
------------------------------------------------------------

> 3 23
------------------------------------------------------------

> 1

item #     amount     category   date            description
------------------------------------------------------------
13         450        apples     2023-01-02      food
15         550        bananas    2023-03-02      morefood
10         200        pears      2020-02-01      gift
14         230        apples     2019-06-13      for_sophia
30         400        maxwell    2019-04-04      birthday
------------------------------------------------------------

> 4
Are you sure you want to delete all transactions? (y/n)
> y
------------------------------------------------------------

> 1
no transactions to print
------------------------------------------------------------

> 0
Quitting . . . Thanks for using this program!
```
