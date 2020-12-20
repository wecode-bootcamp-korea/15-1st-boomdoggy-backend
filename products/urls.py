from django.urls import path
from products.views import TreatView, FoodViews

urlpatterns = [
    path('/our-treats',TreatView.as_view(), name ='our-treats'),
    path('/our-food',FoodViews.as_view(), name ='our-food'),
]
