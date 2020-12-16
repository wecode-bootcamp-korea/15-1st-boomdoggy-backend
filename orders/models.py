from django.db  import  models

from products.models    import  Products


class Orders(models.Model):
    total_cost          =   models.DecimalField(max_digits = 3, decimal_places = 2)
    created_at          =   models.DateTimeField(auto_now_add = True)
    discount_code       =   models.CharField(max_length = 100)
    users                =   models.ForeignKey("users.Users", on_delete = models.CASCADE,default=None)
    payments             =   models.ForeignKey("payments.Payments", on_delete = models.CASCADE,default=None)
    order_status        =   models.ForeignKey("OrderStatus", on_delete = models.CASCADE,default=None)
    payments_types       =   models.ForeignKey("payments.PaymentsType", on_delete = models.CASCADE,default=None)

    class Meta :
        db_table = "orders"

class OrderStatus(models.Model):
    name         =   models.CharField(max_length = 45)

    class Meta :
        db_table = "ordersstatus"

class Carts(models.Model):
    created_at          =   models.DateTimeField(auto_now_add = True)
    quantity            =   models.CharField(max_length=200)
    products            =   models.ForeignKey("products.Products", on_delete = models.CASCADE, default=None)
    users               =   models.ForeignKey("users.Users", on_delete = models.CASCADE,default=None)
    orders               =   models.ForeignKey("Orders", on_delete = models.CASCADE,default=None)
    payments_types       =   models.ForeignKey("payments.PaymentsType", on_delete = models.CASCADE,default=None)

    class Meta :
        db_table = "carts"

class Subscription(models.Model):
    subscription        =   models.BooleanField()
    weeks               =   models.CharField(max_length = 100)
    discount_rate       =   models.IntegerField(default=0)
    users                =   models.ForeignKey("users.Users", on_delete = models.CASCADE, default=None)
    orders               =   models.ForeignKey("Orders", on_delete = models.CASCADE, default=None)

    class Meta :
        db_table = "subscription"

