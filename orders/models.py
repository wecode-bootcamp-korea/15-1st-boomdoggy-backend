from django.db  import  models

from products.models    import  Products


class Orders(models.Model):
    total_cost          =   models.DecimalField(max_digits = 10, decimal_places = 2)
    created_at          =   models.DateTimeField(auto_now_add = True)
    discount_code       =   models.CharField(max_length = 100)
    user                =   models.ForeignKey("users.Users", on_delete = models.CASCADE)
    payment             =   models.ForeignKey("payments.Payments", on_delete = models.CASCADE)
    order_status        =   models.ForeignKey("OrderStatus", on_delete = models.CASCADE)
    payments_type       =   models.ForeignKey("payments.PaymentsType", on_delete = models.CASCADE)

    class Meta :
        db_table = "orders"

class OrderStatus(models.Model):
    name         =   models.CharField(max_length = 45)

    class Meta :
        db_table = "orders_status"

class Carts(models.Model):
    created_at          =   models.DateTimeField(auto_now_add = True)
    quantity            =   models.IntegerField(default=0)
    product             =   models.ForeignKey("products.Products", on_delete = models.CASCADE)
    user                =   models.ForeignKey("users.Users", on_delete = models.CASCADE)
    order               =   models.ForeignKey("Orders", on_delete = models.CASCADE)
    payments_type       =   models.ForeignKey("payments.PaymentsType", on_delete = models.CASCADE)

    class Meta :
        db_table = "carts"

class Subscription(models.Model):
    subscription        =   models.BooleanField(default=False)
    weeks               =   models.CharField(max_length = 100)
    discount_rate       =   models.IntegerField(default=0)
    user                =   models.ForeignKey("users.Users", on_delete = models.CASCADE)
    order               =   models.ForeignKey("Orders", on_delete = models.CASCADE)

    class Meta :
        db_table = "subscription"

