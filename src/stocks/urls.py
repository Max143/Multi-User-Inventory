from django.urls import path
from . import views

urlpatterns = [

    path('stocks/', views.StocksView, name='stocks'),
]

