from    django.db   import models
import  validation  
validate_phone = validation.validate_phone
validate_city = validation.validate_city

class Users(models.Model):
    first_name      =   models.CharField(max_length=100)
    last_name       =   models.CharField(max_length=100)
    email           =   models.EmailField(max_length = 200, verbose_name = "emails", unique = True)
    password        =   models.CharField(max_length = 200)
    annoymous       =   models.SmallIntegerField(default = 0)

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.name

#로그인 후 마이페이지 내에 있는 고객 주소 관리
class Addresses(models.Model):
    user                =   models.ForeignKey('Users', on_delete = models.CASCADE)
    first_name          =   models.CharField(max_length = 200)
    last_name           =   models.CharField(max_length = 200)
    address             =   models.CharField(max_length = 500)
    appartment_type     =   models.CharField(max_length = 500)
    city                =   models.CharField(max_length = 200, validators=[validate_city], blank = False)
    county_region       =   models.CharField(max_length = 100)
    postcode            =   models.CharField(max_length = 50)
    phone_number        =   models.CharField(max_length = 50, validators=[validate_phone], blank = False)

    class Meta:
        db_table = "address"

    def __str__(self):
        return self.name


