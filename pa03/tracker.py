''' tracker.py - a command line program to track transactions '''

import sys
from transactions import Transaction

#written by jack + ken + kevin
def print_usage():
    ''' print an explanation of how to use this command '''
    print('''Enter a number to execute that command:
            0. quit
            1. show transactions
            2. add transaction
                Usage: \"2 item_no amount category YYYY-MM-DD description\"
            3. delete transaction
                Usage: \"3 item_no\"
            4. delete all tran5sactions
            5. summarize transactions by date
                Usage: \"5 YYYY-MM-DD\" for items from the given date
                    or \"5\" for all items sorted by date
            6. summarize transactions by month
                Usage: \"6 MM\"
                    or \"6 YYYY-MM\"
            7. summarize transactions by year
                Usage: \"7 YYYY\"
            8. summarize transactions by category
                Usage: \"8 category\"
            9. print this menu
            '''
          )

#written by kevin
def print_transactions(transactions):
    ''' print the transaction items '''
    if len(transactions) == 0:
        print('no transactions to print')
        return
    print("\n%-10s %-10s %-10s %-15s %-30s" %
          ('item #', 'amount', 'category', 'date', 'description'))
    print('-'*60)
    for item in transactions:
        values = tuple(item.values())  # (rowid,title,desc,completed)
        # print(values)

        print("%-10s %-10s %-10s %-15s %-30s" % values)

#written by ken + kevin + jack
def process_args(arglist):
    ''' examine args and make appropriate calls to transactions '''
    trans = Transaction('transactions.db')

    if arglist[0] == "1":
        print_transactions(trans.show())

    elif arglist[0] == '2':
        if len(arglist) != 6:
            print(
                "Incorrect syntax\nUsage: \"2 item_no amount category YYYY-MM-DD description\"\n")
        else:
            todo = {'item_no': arglist[1], 'amount': arglist[2],
                    'category': arglist[3], 'date': arglist[4], 'desc': arglist[5]}
            trans.add(todo)

    elif arglist[0] == '3':
        if len(arglist) != 2:
            print("Incorrect syntax\nUsage: \"3 item_no\"\n")
        else:
            trans.delete(arglist[1])

    elif arglist[0] == '4':
        confirm = input(
            "Are you sure you want to delete all transactions? (y/n)\n> ")
        if confirm in ('y', 'Y'):
            trans.clear()
        else:
            print("Did not delete all transactions\n")

    elif arglist[0] == '5':
        if len(arglist) == 1:
            print("Transactions sorted by date: ")
            print_transactions(trans.sort_date())
        elif len(arglist) == 2:
            print("Transactions from ", arglist[1], ": ", sep='')
            print_transactions(trans.summary_date(arglist[1]))
        else:
            print("Incorrect syntax\nUsage: \"5 YYYY-MM-DD\" or \"5\"\n")

    elif arglist[0] == '6':
        if len(arglist) == 2:
            if len(arglist[1].split('-')) == 1:
                print("Transactions from month ", arglist[1], ": ", sep='')
                print_transactions(trans.summary_month(arglist[1]))
            elif len(arglist[1].split('-')) == 2:
                print("Transactions from ", arglist[1], ": ", sep='')
                print_transactions(trans.summary_month_year(arglist[1]))
            else:
                print("Incorrect syntax\nUsage: \"6 MM\" or \"6 YYYY-MM\"\n")
        else:
            print("Incorrect syntax\nUsage: \"6 MM\" or \"6 YYYY-MM\"\n")

    elif arglist[0] == '7':
        if len(arglist) != 2:
            print("Incorrect syntax\nUsage: \"7 YYYY\"\n")
        else:
            print("Transactions from ", arglist[1], ": ", sep='')
            print_transactions(trans.summary_year(arglist[1]))

    elif arglist[0] == '8':
        if len(arglist) != 2:
            print("Incorrect syntax\nUsage: \"8 category\"\n")
        else:
            print("Transactions from the ", arglist[1], " category: ", sep='')
            print_transactions(trans.summary_category(arglist[1]))

    elif arglist[0] == "9":
        print_usage()

    else:
        print(arglist[0], "is not implemented\n")

#written by jack + kevin
def main():
    ''' top level function to process command line args and prompt for input '''
    if len(sys.argv) == 1:  # no arguments passed, prompt for them in a loop
        print_usage()
        args = []
        while args != ['']:
            args = input("> ").split(' ')
            if args[0] == "0":
                break
            if args != ['']:
                process_args(args)
            print('-'*60+'\n')
        print("Quitting . . . Thanks for using this program!")
    else:  # arguements passed, read and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*60+'\n')


main()