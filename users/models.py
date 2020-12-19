from    django.db   import models
import  validation  
validate_phone = validation.validate_phone
validate_city = validation.validate_city

class Users(models.Model):
    first_name      =   models.CharField(max_length=100)
    last_name       =   models.CharField(max_length=100)
    email           =   models.EmailField(max_length = 200, verbose_name = "emails", unique = True)
    password        =   models.CharField(max_length = 200)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.name

class AddressList(models.Model):
    first_name          =   models.CharField(max_length = 200)
    last_name           =   models.CharField(max_length = 200)
    address             =   models.CharField(max_length = 500)
    appartment_type     =   models.CharField(max_length = 500)
    city                =   models.CharField(max_length = 200, validators=[validate_city], blank = False)
    county_region       =   models.CharField(max_length = 100)
    postcode            =   models.CharField(max_length = 50)
    phone_number        =   models.CharField(max_length = 50, validators=[validate_phone], blank = False)
    company             =   models.CharField(max_length = 100)
    user                =   models.ForeignKey('Users', on_delete = models.CASCADE)

    class Meta:
        db_table = "address_list"

    def __str__(self):
        return self.name

