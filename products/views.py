import json

from django.http    import JsonResponse
from django.views   import View

from products.models import Categories, Images, Products, Sale, Review
from orders.models   import Options

class ProductListView(View):
    def get(self,request):
        category    = request.GET.get('name', None)
        products    = Products.objects.all()

        if category == "ourfoods":
            treats = Categories.objects.get(name="treats")
            products = Products.objects.exclude(category_id = treats)
        elif category == "allfoods":
            products = Products.objects.all()

        else:
            category_id = Categories.objects.get(name=category).id
            products    = Products.objects.filter(category_id=category_id)

        products_list = [{
        "id"            : product.id,
        "name"          : product.name,
        "main_image"    : Products.objects.get(id = product.id).images_set.all().first().image_url,
        "sub_image"     : Products.objects.get(id = product.id).images_set.all().last().image_url,
        "category"      : product.category.name,
        "price"         : product.price,
        "stock"         : product.stock_status,
        "sale_rate"     : product.sale_rate.sale_rate} for product in products]
        return JsonResponse({"products_list":products_list}, status=200)

class ProductDetailView(View):
    def get(self,request, product_id):
        try:
            product = Products.objects.get(id=product_id)
            option = Options.objects.all()
            data = {
                "id"            : product.id,
                "name"          : product.name,
                "main_image"    : Products.objects.get(id=product_id).images_set.all().first().image_url,
                "sub_image"     : Products.objects.get(id=product_id).images_set.all().last().image_url,
                "category"      : Products.objects.get(id=1).category.name,
                "description"   : product.description,
                "benefits"      : product.benefit,
                "ingredients"   : product.ingredients,
                "price"         : product.price,
                "stock"         : product.stock_status,
                "sale_rate"     : product.sale_rate.sale_rate,
                "kg_2"          : option[0].kilogram,
                "kg_6"          : option[1].kilogram,
                "kg_12"         : option[2].kilogram,
                "kg_2_rate"     : option[0].rate,
                "kg_6_rate"     : option[1].rate,
                "kg_12_rate"    : option[2].rate,
                }
            return JsonResponse({"products_detail":data}, status=200)
        except Products.DoesNotExist:
            return JsonResponse({"message":"NOT_FOUND"},status=401)


class ProductReviewView(View):
    def get(self,request):
        reviews = Review.objects.all()
        review_list = [{
            "id"                : review.id,
            "name"              : review.name,
            "image"             : review.image_url,
            "content"           : review.content,
            "date"              : review.created_at,
            "content_rating"    : review.content_rating,
        }for review in reviews]
        return JsonResponse({"review_list":review_list}, status=200)
