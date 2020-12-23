from django.urls import path
from products.views import ProductListView, ProductReviewView, ProductDetailView
urlpatterns = [
    path('',ProductListView.as_view()),
    path('/boomdoggy',ProductReviewView.as_view()),
    path('/detail/<int:product_id>', ProductDetailView.as_view()),
]
