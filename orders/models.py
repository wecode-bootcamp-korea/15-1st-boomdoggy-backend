from django.db  import  models

from products   import  models
from payments   import  models
from user       import  models

class Orders(models.Model):
    total_cost               =   models.DecimalField(max_digits = 3, decimal_places = 2)
    created_at          =   models.DateTimeField(auto_now_add = True)
    discount_code       =   models.CharField(max_length = 100)
    user_id             =   models.ForeignKey("Users", on_delete = models.CASCADE)
    payment_id          =   models.ForeignKey("Payments", on_delete = models.CASCADE)
    oder_status_id      =   models.ForeignKey("OrderStatus", on_delete = models.CASCADE)
    payment_id          =   models.ForeignKey("PaymentsType", on_delete = models.CASCADE)

    class Meta :
        db_data = ‘order’

class OrderStatus(models.Model):
    name         =   models.CharField(max_length = 45)

    class Meta :
        db_data = "orders_status"

class Carts(models.Model):
    created_at          =   models.DateTimeField(auto_now_add = True)
    quantity            =   models.CharField(max_length=200)
    product_id          =   models.ForeignKey("Products", on_delete = models.CASCADE)
    user_id             =   models.ForeignKey("Users", on_delete = models.CASCADE)
    order_id            =   models.ForeignKey("Orders", on_delete = models.CASCADE)
    payment_id          =   models.ForeignKey("PaymentsType", on_delete = models.CASCADE)

    class Meta :
        db_data = "cart"

class Subscriptions(models.Model):
    subscription        =   models.BooleanField(default = False)
    weeks               =   models.CharField(max_length = 100)
    discount_rate       =   models.IntegerField(default=0)
    user_id             =   models.ForeignKey("Users", on_delete = models.CASCADE)
    order_id            =   models.ForeignKey("Orders", on_delete = models.CASCADE)
    product_id          =   models.ForeignKey("Products", on_delete = models.CASCADE)

    class Meta :
        db_data = "subscription"

