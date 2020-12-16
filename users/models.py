from django.db import models

class Users(models.Model):
    first_name      =   models.CharField(max_length=100)
    last_name       =   models.CharField(max_length=100)
    email           =   models.EmailField(max_length = 200, verbose_name = "emails", unique = True)
    password        =   models.CharField(max_length = 200)
    annoymous       =   models.SmallIntegerField(default = 0)

    class Meta :
        db_table = "Users"

    def __str__(self):
        return self.name



class Addresses(models.Model):
        user_id         =   models.ForeignKey("Users", on_delete = models.CASCADE)
        address         =   models.CharField(max_length = 200)

    class Meta :
        db_data = "address"

    def __str__(self):
        return self.name


