from django.urls import path
from . import views

urlpatterns = [
    #Sets the url path to home page index.html
    path('', views.home, name='index'),
    # path to Create account CreateNewAccount.html
    path('create/', views.create_account, name='create'),
    #Sets the url path to Balance sheet page BalanceSheet.html
    path('<int:pk>/balance/', views.balance, name='balance'),
    #url path New Transaction AddNewTransaction.html
    path('transaction/', views.transaction, name='transaction')
]
