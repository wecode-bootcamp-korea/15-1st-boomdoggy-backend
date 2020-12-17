from django.db import models

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


class Addresses(models.Model):
    user            =   models.ForeignKey("Users", on_delete = models.CASCADE)
    address         =   models.CharField(max_length = 200)

    class Meta:
        db_table = "address"

    def __str__(self):
        return self.name


