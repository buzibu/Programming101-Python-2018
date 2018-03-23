# Money Tracker

In a file called `money_tracker.py` implement a program that tracks user incomes and expenses.
We are going to use the TDD approach to create our small application. Write your tests in `test_money_tracker.py`.

Your application must have the following functionalities:
- Show all user data(incomes and expenses).
- Show user data for specific date.
- Lists all expense categories.
- Lists all income categories.
- The user can add new income or expense for specific date and category.
- The user must be able to create new categories.

In the `money_tracker.py` module you must have these methods:

```python
def list_user_data():
    pass


def show_user_savings():
    pass


def show_user_deposits():
    pass


def show_user_expenses():
    pass


def list_user_expenses_ordered_by_categories():
    pass


def show_user_data_per_date(date):
    pass


def list_income_categories():
    pass


def list_expense_categories():
    pass


def add_income(income_category, money, date):
    pass


def add_expense(expense_category, money, date):
    pass
```

The user data is going to be saved in a file called `money_tracker.txt`. In order to have a working program, you should parse the information saved in the file. The `modey_tracker.txt` has a specific format:
```txt
=== 22-03-2018 ===
760, Salary, New Income
5.5, Eating Out, New Expense
34, Clothes, New Expense
41.79, Food, New Expense
12, Eating Out, New Expense
7, House, New Expense
14, Pets, New Expense
112.40, Bills, New Expense
21.5, Transport, New Expense
=== 23-03-2018 ===
50, Savings, New Income
15, Food, New Expense
200, Deposit, New Income
5, Sports, New Expense
```

The following test example is based on the data in the `money_tracker.txt`
## Examples:
```python
Hello, Peter!
Choose one of the following options to continue:
1 - show all data
2 - show data for specific date
3 - show expenses, ordered by categories
4 - add new income
5 - add new expense
6 - exit
>>> 1
=== 22-03-2018 ===
760, Salary, New Income
5.5, Eating Out, New Expense
34, Clothes, New Expense
41.79, Food, New Expense
12, Eating Out, New Expense
7, House, New Expense
14, Pets, New Expense
112.40, Bills, New Expense
21.5, Transport, New Expense
=== 23-03-2018 ===
50, Savings, New Income
15, Food, New Expense
200, Deposit, New Income
5, Sports, New Expense


Choose one of the following options to continue:
1 - show all data
2 - show data for specific date
3 - show expenses, ordered by categories
4 - add new income
5 - add new expense
6 - exit
>>> 4
New income amount:
>>> 10
New income type:
>>> Deposit
New income date:
23-03-2018


Choose one of the following options to continue:
1 - show all data
2 - show data for specific date
3 - show expenses, ordered by categories
4 - add new income
5 - add new expense
6 - exit
>>> 1
=== 22-03-2018 ===
760, Salary, New Income
5.5, Eating Out, New Expense
34, Clothes, New Expense
41.79, Food, New Expense
12, Eating Out, New Expense
7, House, New Expense
14, Pets, New Expense
112.40, Bills, New Expense
21.5, Transport, New Expense
=== 23-03-2018 ===
50, Savings, New Income
15, Food, New Expense
200, Deposit, New Income
5, Sports, New Expense
10, Deposit, New income


Choose one of the following options to continue:
1 - show all data
2 - show data for specific date
3 - show expenses, ordered by categories
4 - add new income
5 - add new expense
6 - exit
```

## Test Examples:
```python
>>> show_user_savings()
[(10, 'Deposit'), (200, 'Deposit'), (50, 'Savings'), (760, 'Salary')]
>>> list_user_expenses_ordered_by_categories()
[(112.40, 'Bills'), (34, 'Clothes'), (5.5, 'Eating Out'), (12, 'Eating Out'), (15, 'Food'), (41.79, 'Food'), (7, 'House'), (14, 'Pets'), (5, 'Sports'), (21.5, 'Transport')]
>>> show_user_data_per_date('23-03-2018')
[(50, 'Savings', 'New Income'), (15, 'Food', 'New Expense'), (200, 'Deposit', 'New Income'), (5, 'Sports', 'New Expense'), (10, 'Deposit', 'New income')]  
>>> list_income_categories()
['Salary', 'Deposit', 'Savings']   
>>> add_income('Salary', 600, '25-03-2018')
>>> add_expense('Health', 2.5, '25-03-2018')

```
