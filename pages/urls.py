from django.urls import path
from . import views

urlpatterns = [
	path('',views.home, name="home"),
	path('trade.html',views.trade, name="trade"),
	path('rent.html',views.rent, name="rent"),
	path('import_trade.html',views.import_trade, name="import_trade"),
	path('import_rent.html',views.import_rent, name="import_rent"),
	path('delete_trade.html',views.delete_trade, name="delete_trade"),
	path('delete_trent.html',views.delete_rent, name="delete_rent"),
]
