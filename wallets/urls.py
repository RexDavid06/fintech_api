from django.urls import path
from . import views 

urlpatterns = [
    path('walletBalance/', views.WalletView.as_view()),
]