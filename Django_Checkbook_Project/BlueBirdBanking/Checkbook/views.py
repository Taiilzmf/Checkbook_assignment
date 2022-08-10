from urllib import request

# import Transactions as Transactions
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


# this function will render the home page when requested
def home(request):
    form = TransactionForm(data=request.POST or None)  # retrieve acct form
    # checks request method is post
    if request.method == 'POST':
        pk = request.POST['account']  # if form submitted retrieve account user wants to view
        return balance(request, pk)  # call balance
    content = {'form': form}  # saves content to template as dictionary
    # adds content to form
    return render(request, 'checkbook/index.html', content)


# function will render the create new account page
def create_account(request):
    form = AccountForm(data=request.POST or None)  # retrieve acct form
    # checks request method is post
    if request.method == 'POST':
        if form.is_valid():  # checks to see if submitted form is valid if so saves form
            form.save()  # saves new account
            return redirect('index')  # returns user to home page
    content = {'form': form}  # saves content to template as dictionary
    # adds content to form
    return render(request, 'checkbook/CreateNewAccount.html', content)


# function will render the balance page
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk)  # retrieve acct using primary key
    transactions = Transaction.Transactions.filter(account=pk)  # retrieve all acct transactions
    current_total = account.initial_deposit  # create acct total variable starting w/ initial deposit
    table_contents = {}  # creates dictionary into which transaction info will be placed
    for t in transactions:  # loop
        if t.type == 'Deposit':
            current_total += t.amount  # deposit add to amount
            table_contents.update({t: current_total})  # add transaction and total to the dictionary
        else:
            current_total -= t.amount  # withdraw subtract
            table_contents.update({t: current_total})
    # pass acct, acct total, and transaction info to template
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


# function will render the Transaction page
def transaction(request):
    form = TransactionForm(data=request.POST or None)  # retrieve acct form
    # checks request method is post
    if request.method == 'POST':
        if form.is_valid():  # checks to see if submitted form is valid if so saves form
            pk = request.POST['account']
            form.save()  # saves new account
            return balance(request, pk)  # returns user to home page
    content = {'form': form}  # saves content to template as dictionary
    # adds content to form
    return render(request, 'checkbook/AddTransaction.html', content)
