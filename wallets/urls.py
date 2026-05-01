from django.urls import path
from . import views 

urlpatterns = [
    path('balance/', views.WalletView.as_view()),
]