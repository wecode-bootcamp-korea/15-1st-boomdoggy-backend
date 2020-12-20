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
    total_price         =   models.DecimalField(max_digits = 10, decimal_places = 2)
    payments_type       =   models.ForeignKey("payments.PaymentsType", on_delete = models.CASCADE)

    class Meta :
        db_table = "carts"

    def __str__(self):
        return self.name

class OptionKilograms(models.Model): 
    kilogram            =   models.IntegerField(default = 2)
    rate                =   models.IntegerField(default = 0)

    class Meta:
        db_table = "option_kilograms"

    def __str__(self):
        return self.name

class OptionPieces(models.Model):
    piece               =   models.IntegerField(default = 5)
    rate                =   models.IntegerField(default = 0)
    
    class Meta:
        db_table = "option_pieces"

    def __str__(self):
        return self.name


class Options(models.Model):
    optionkilograms     =   models.ForeignKey('OptionKilograms', on_delete = models.CASCADE)
    optionpieces        =   models.ForeignKey('OptionPieces', on_delete = models.CASCADE)
    product             =   models.ForeignKey("products.Products", on_delete = models.CASCADE)

    class Meta:
        db_table = "options"

    def __str__(self):
        return self.name
