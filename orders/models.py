from django.db  import  models

from products.models    import  Products


class Orders(models.Model):
    created_at          =   models.DateTimeField(auto_now_add = True)
    user                =   models.ForeignKey("users.Users", on_delete = models.CASCADE)
    payment             =   models.ForeignKey("payments.Payments", on_delete = models.CASCADE)
    order_status        =   models.ForeignKey("OrderStatus", on_delete = models.CASCADE)

    class Meta :
        db_table = "orders"

    def __str__(self):
        return self.name


class OrderStatus(models.Model):
    name         =   models.CharField(max_length = 45)

    class Meta :
        db_table = "orders_status"

    def __str__(self):
        return self.name

class Carts(models.Model):
    created_at          =   models.DateTimeField(auto_now_add = True)
    quantity            =   models.IntegerField(default=0)
    product             =   models.ForeignKey("products.Products", on_delete = models.CASCADE)
    order               =   models.ForeignKey("Orders", on_delete = models.CASCADE)
    total_price         =   models.IntegerField(default=0)
    sub_total           =   models.IntegerField(default=0)
    payments_type       =   models.ForeignKey("payments.PaymentsType", on_delete = models.CASCADE)
    option              =   models.ForeignKey("Options",on_delete = models.CASCADE)

    class Meta :
        db_table = "carts"

class ProductOption(models.Model):
    option              =   models.ForeignKey("Options", on_delete = models.CASCADE)
    product             =   models.ForeignKey("products.Products", on_delete = models.CASCADE)

    class Meta:
        db_table = "option_kilograms"

class Options(models.Model):
    kilogram            =   models.IntegerField(default = 0)
    rate                =   models.IntegerField(default = 0)
    option              =   models.ManyToManyField("products.Products" , through= "ProductOption")

    class Meta:
        db_table = "options"

