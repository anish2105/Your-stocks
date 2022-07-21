from django.urls import path,include
from . import views

urlpatterns = [
    path('stockindex/',views.stockpage,name = 'stockpage'),
    path('addstock/',views.addstock,name = 'addstock'),
    path('stats/',views.stats,name = 'stats'),
]
