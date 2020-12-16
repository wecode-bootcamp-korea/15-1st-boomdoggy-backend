from django.db      import models


class Categories(models.Model):
    name    = models.CharField(max_length = 200)

    class Meta:
        db_table = "categories"

    def __str__(self):
        return self.name

class Products(models.Model):
    categories      = models.ForeignKey("Categories", on_delete = models.CASCADE)
    name            = models.CharField(max_length = 100, unique=True)
    review_ratings  = models.SmallIntegerField(blank= True)
    prices          = models.DecimalField(max_digits = 3, decimal_places = 2)
    pieces          = models.CharField(max_length = 100, blank = True)
    kilograms       = models.CharField(max_length = 100, blank = True)
    subscription    = models.ForeignKey("orders.Subscription", on_delete = models.CASCADE)
    quantity        = models.CharField(max_length = 100)
    descriptions    = models.CharField(max_length = 1000)
    benefits        = models.CharField(max_length = 1000)
    ingredients     = models.CharField(max_length = 1000)
    stock_rate      = models.IntegerField(default=0)
    sale_rate       = models.IntegerField(default=0)


    class Meta:
        db_table = "products"

    def __str__(self):
        return self.name

class ImagesProducts(models.Model):
    images      = models.ForeignKey("Images", on_delete = models.CASCADE)
    products    = models.ForeignKey("Products", on_delete = models.CASCADE)

    class Meta:
        db_table = "images_products"

class Images(models.Model):
    image_url    = models.CharField(max_length=2000)
    images          = models.ManyToManyField(Products, through = "ImagesProducts")

    class Meta:
        db_table = "images"

    def __str__(self):
        return self.name

class Review(models.Model):
    name            = models.CharField(max_length = 100)
    created_at      = models.DateTimeField(auto_now_add = True)
    reviews         = models.CharField(max_length =1000)
    review_ratings  = models.IntegerField(default = 0)
    img_url         = models.CharField(max_length = 500)
    category        = models.ForeignKey("Categories", on_delete = models.CASCADE)
    products         = models.ForeignKey("Products", on_delete = models.CASCADE)

    class Meta:
        db_table = "reviews"

    def __str__(self):
        return self.name


