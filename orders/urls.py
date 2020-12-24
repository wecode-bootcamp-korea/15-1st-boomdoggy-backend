from django.urls    import path
from orders.views   import Cart
from users.views    import SignIn, Address

urlpatterns = [
    path('/cart', Cart.as_view()),
]

