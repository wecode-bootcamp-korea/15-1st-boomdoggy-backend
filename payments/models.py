from django.db  import models

from users.models       import Users
from orders.models      import Orders
import validation
validate_phone = validation.validate_phone
validate_city = validation.validate_city

class Payments(models.Model):
    first_name          =   models.CharField(max_length = 200)
    last_name           =   models.CharField(max_length = 200)
    address             =   models.CharField(max_length = 500)
    appartment_type     =   models.CharField(max_length = 500)
    city                =   models.CharField(max_length = 200, validators=[validate_city], blank = False)
    county_region       =   models.CharField(max_length = 100)
    postcode            =   models.CharField(max_length = 50)
    phone_number        =   models.CharField(max_length = 50, validators=[validate_phone], blank = False)
    user                =   models.ForeignKey("users.Users",on_delete = models.CASCADE)

    class Meta:
        db_table = "payments"
    
    def __str__(self):
        return self.name


class Shipping(models.Model):
    name                =   models.CharField(max_length = 200)
    shipping_fee        =   models.DecimalField(max_digits = 10, decimal_places = 2)
    order               =   models.ForeignKey("orders.Orders", on_delete = models.CASCADE)

    class Meta:
        db_table = "shipping"
    
    def __str__(self):
        return self.name

class PaymentsCard(models.Model):
    users                =   models.ForeignKey("users.Users", on_delete = models.CASCADE)
    payments            =   models.ForeignKey("Payments", on_delete = models.CASCADE)
    payments_types      =   models.ForeignKey("PaymentsType", on_delete = models.CASCADE)

    class Meta:
        db_table = "payments_card"

    def __str__(self):
        return self.name

class PaymentsType(models.Model):
    payments_module_name    =   models.CharField(max_length = 100)

    class Meta:
        db_table = "payments_type"

    def __str__(self):
        return self.name
