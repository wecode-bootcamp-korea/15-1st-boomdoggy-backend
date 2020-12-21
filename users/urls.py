from django.urls    import path
from users.views    import SignUp, SignIn, Address

urlpatterns = [
    path('/signup', SignUp.as_view()),
    path('/signin', SignIn.as_view()),
    path('/addresses', Address.as_view()),
]
