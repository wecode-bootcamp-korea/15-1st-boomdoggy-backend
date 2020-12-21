from django.urls import path
from products.views import ProductListView

urlpatterns = [
    path('/category',ProductListView.as_view()),
    #path('/category/<int:product_id>', ProductDetailView.as_view()),
]
