from django.urls import path
from . import views

urlpatterns = [
    # sets url path to home page index.html
    path('', views.home, name='index'),
    # sets url path to create new account page CreateNewAccount.html
    path('create/', views.create_account, name='create'),
    # sets url path to balance sheet page BalanceSheet.html
    path('<int:pk>/balance/', views.balance, name='balance'),
    # sets the url path to add new transaction page addnewtransaction.html
    path('transaction/', views.transaction, name='transaction')
]
