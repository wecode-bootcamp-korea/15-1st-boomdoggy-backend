from django.db      import models

class Categories(models.Model):
    name    = models.CharField(max_length = 200)

    class Meta:
        db_table = "categories"

    def __str__(self):
        return self.name

class Products(models.Model):
    category        = models.ForeignKey("Categories", on_delete = models.CASCADE)
    name            = models.CharField(max_length = 100, unique=True)
    review_rating   = models.SmallIntegerField(blank= True)
    price           = models.DecimalField(max_digits = 10, decimal_places = 2)
    piece           = models.CharField(max_length = 100, blank = True)
    kilogram        = models.IntegerField(default = 0)
    subscription    = models.ForeignKey("orders.Subscription", on_delete = models.CASCADE)
    quantity        = models.IntegerField(default=0)
    description     = models.TextField()
    benefit         = models.CharField(max_length = 1000)
    ingredients     = models.CharField(max_length = 1000)
    stock_rate      = models.IntegerField(default=0)
    sale_rate       = models.IntegerField(default=0)
    image           = models.ForeignKey("Images", on_delete = models.CASCADE)

    class Meta:
        db_table = "products"

    def __str__(self):
        return self.name

class Images(models.Model):
    image_url       = models.CharField(max_length=2000)

    class Meta:
        db_table = "images"

    def __str__(self):
        return self.name

class Review(models.Model):
    name            = models.CharField(max_length = 100)
    created_at      = models.DateTimeField(auto_now_add = True)
    content         = models.CharField(max_length =1000)
    content_rating  = models.IntegerField(default = 0)
    image_url       = models.CharField(max_length = 500)
    category        = models.ForeignKey("Categories", on_delete = models.CASCADE)
    product         = models.ForeignKey("Products", on_delete = models.CASCADE)

    class Meta:
        db_table = "reviews"

    def __str__(self):
        return self.name


