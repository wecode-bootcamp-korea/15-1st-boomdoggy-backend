from django.urls import path
from products.views import TreatView, FoodViews, AdultFoodViews, SuperFoodViews, PuppyFoodViews ,LightFoodViews

urlpatterns = [
    path('/our-treats',TreatView.as_view(), name ='our-treats'),
    path('/our-food',FoodViews.as_view(), name ='our-food'),
    path('/adult-food',AdultFoodViews.as_view(), name="adult-foods"),
    path('/super-food',SuperFoodViews.as_view(), name="super-foods"),
    path('/puppy-food',PuppyFoodViews.as_view(), name="puppy-foods"),
    path('/light-food',LightFoodViews.as_view(), name="light-foods"),
]
