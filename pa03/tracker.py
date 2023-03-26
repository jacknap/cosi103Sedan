import sys
from transaction import Transaction


# here are some helper functions ...

def print_usage():
    ''' print an explanation of how to use this command '''
    print('''Enter a number to execute that command:
            0. quit
            4. show transactions
            5. add transaction
            6. delete transaction
            7. summarize transactions by date
            8. summarize transactions by month
            9. summarize transactions by year
            10. summarize transactions by category
            11. print this menu
            '''
          )


def print_transactions(todos):
    ''' print the todo items '''
    if len(todos) == 0:
        print('no transactions to print')
        return
    print('\n')
    print("%-10s %-10s %-10s %-15s %-30s" %
          ('item #', 'amount', 'category', 'date', 'desc'))
    print('-'*60)
    for item in todos:
        values = tuple(item.values())  # (rowid,title,desc,completed)
        # print(values)

        print("%-10s %-10s %-10s %-15s %-30s" % values)


def process_args(arglist):
    ''' examine args and make appropriate calls to transactions '''
    trans = Transaction('transaction.db')
    if arglist == []:
        print_usage()

    elif arglist[0] == "4":
        print_transactions(trans.show())
    elif arglist[0] == '5':
        if len(arglist) != 6:
            print_usage()
        else:
            todo = {'item_no': arglist[1], 'amount': arglist[2],
                    'category': arglist[3], 'date': arglist[4], 'desc': arglist[5]}
            trans.add(todo)
    elif arglist[0] == '6':
        if len(arglist) != 2:
            print_usage()
        else:
            trans.delete(arglist[1])
    elif arglist[0] == '7':
        print("Sorting by date : ")
        print_transactions(trans.sumbydate())
    elif arglist[0] == '8':
        print("Sorting by month : ")
        print_transactions(trans.sumbymonth())
    elif arglist[0] == '9':
        print("Sorting by year : ")
        print_transactions(trans.sumbyyear())
    elif arglist[0] == 'delete':
        trans.clear()
    elif arglist[0] == "11":
        print_usage()
    else:
        print(arglist[0], "is not implemented\n")
        print_usage()


def main():
    ''' top level function to process command line args and prompt for input '''
    if len(sys.argv) == 1:  # no arguments passed, prompt for them in a loop
        print_usage()
        args = []
        while args != ['']:
            args = input("> ").split(' ')
            if args[0] == "0":
                break
            elif args != ['']:
                process_args(args)
            # elif args[0]=='add':
            #     # join everyting after the name as a string
            #     args = ['add',args[1]," ".join(args[2:])]

            print('-'*60+'\n'*2)
        print("Quitting . . . Thanks for using this program!")
    else:
        # arguements passed, read and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*60+'\n'*2)


main()
