
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


# Function will render home when asked
def home(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        pk = request.POST['account']
        return balance(request, pk)  # calls balance function to te accounts balance sheet
    content = {'form': form}
    return render(request, 'checkbook/index.html', content)

# function will render the Create New Account page when asked

# will display balance sheet when asked
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk)
    transactions = Transaction.Transactions.filter(account=pk)
    current_total = account.initial_deposit
    table_contents = {}  # create a dictionary  into which transaction information wil be placed
    for t in transactions:
        if t.type == 'Deposit':
            current_total += t.amount
            table_contents.update({t: current_total})
        else:
            current_total -= t.amount
            table_contents.update({t: current_total})
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)

# will display transaction sheet when asked


def create_account(request):
    form = AccountForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index') #Returns User back to the home page
    content = {'form': form} #Saves content to the template as a dictionary
    # adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html', content)

# This function will render to Transaction page when requested
def transaction(request):
    form = TransactionForm(request.POST or None)
    # Checks if request method is Post
    if request.method == 'POST':
        if form.is_valid():  # checks to see if the form is valid
            pk = request.POST['account']
            form.save()
            return balance(request, pk)  # Renders balance of the accounts balance sheet
    # pass content to the template in a dictionary
    content = {'form': form}
    # adds content of form to the page
    return render(request, 'checkbook/AddTransaction.html', content)

