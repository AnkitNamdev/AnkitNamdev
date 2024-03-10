
from django.urls import path
from . import views

urlpatterns = [
   path('',views.home),
   path('new',views.home1),
   path('daily',views.dailyproduct,name="dailyprod"),
   path('sports',views.sports,name="sports"),
   path('allitem',views.allitem,name="allitems"),
   path('buy/<int:id>/<price>/<av>',views.buy, name="buy"),
   path('balling',views.bill,name="billing"),
   path('bill',views.delivery,name='bill')

]