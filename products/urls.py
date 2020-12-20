from django.urls import path
from products.views import TreatView

urlpatterns = [
    path('/our-treats',TreatView.as_view(), name ='our-treats'),
]
