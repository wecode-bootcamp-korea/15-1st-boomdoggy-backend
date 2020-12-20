import json

from django.http    import JsonResponse
from django.views   import View

from products.models import Categories, Images, Products

class TreatViews(View):
    def get(self,request):
        treats      = Categories.objects.get(name="treats")
        products    = Products.objects.filter(category_id = treats)

        treats    = Products.objects.filter(category_id = treats)

        treats_list = [{
            "id"            : treats[i].id,
            "name"          : treats[i].name,
            "main_image"    : Images.objects.filter(product_id = treats[i].id).first().image_url,
            "sub_image"     : Images.objects.filter(product_id = treats[i].id).last().image_url,
            "category"      : treats[i].category.name,
            "price"         : treats[i].price,
            "stock"         : treats[i].stock_status,
            "sale_rate"     : treats[i].sale_rate.sale_rate}for i in range(len(treats))]

        return JsonResponse({"treats_list" : treats_list}, status=200)

class FoodViews(View):
    def get(self,request):
        foods    = Products.objects.exclude(category_id =treats)

        foods_list = [{
            "id"            : foods[i].id,
            "name"          : foods[i].name,
            "main_image"    : Images.objects.filter(product_id = foods[i].id).first().image_url,
            "sub_image"     : Images.objects.filter(product_id = foods[i].id).last().image_url,
            "category"      : foods[i].categroy.name,
            "price"         : foods[i].price,
            "stock"         : foods[i].stock_status,
            "sale_rate"     : foods[i].sale_rate.sale_rate} for i in range(len(foods))]

        return JsonResponse({"foods_list":foods_list}, status=200)

class AdultFoodViews(View):
    def get(self,request):
        adult_foods = Categories.objects.get(name="Adult Food")
        adult_foods = Products.objects.filter(category_id =adult_foods)

        adult_foods_list = [{
            "id"            : adult_foods[i].id,
            "name"          : adult_foods[i].name,
            "main_image"    : Images.objects.filter(product_id = adult_food[i].id).first().image_url,
            "sub_image"     : Images.objects.filter(product_id = adult_food[i].id).last().image_url,
            "category"      : adult_foods[i].categroy.name,
            "price"         : adult_foods[i].price,
            "stock"         : adult_foods[i].stock_status,
            "sale_rate"     : adult_foodsfoods[i].sale_rate.sale_rate} for i in range(len(adult_foods))]

        return JsonResponse({"foods_list":foods_list}, status=200)

class PuppyFoodViews(View):
    def get(self,request):
        puppy = Categories.objects.get(name="Puppy Food")
        puppy_foods = Products.objects.filter(category_id =puppy)

        puppy_foods_list = [{
            "id"            : puppy_foods[i].id,
            "name"          : puppy_foods[i].name,
            "main_image"    : Images.objects.filter(product_id = puppy_foods[i].id).first().image_url,
            "sub_image"     : Images.objects.filter(product_id = puppy_foods[i].id).last().image_url,
            "category"      : puppy_foods[i].categroy.name,
            "price"         : puppy_foods[i].price,
            "stock"         : puppy_foods[i].stock_status,
            "sale_rate"     : puppy_foods[i].sale_rate.sale_rate} for i in range(len(puppy_foods))]

        return JsonResponse({"puppy_foods_list":puppy_foods_list}, status=200)

class SuperFoodViews(View):
    def get(self,request):
        superfoods = Categories.objects.get(name="Super Food")
        super_foods = Products.objects.filter(category_id =superfoods)

        super_foods_list = [{
            "id"            : super_foods[i].id,
            "name"          : super_foods[i].name,
            "main_image"    : Images.objects.filter(product_id = super_foods[i].id).first().image_url,
            "sub_image"     : Images.objects.filter(product_id = super_foods[i].id).last().image_url,
            "category"      : super_foods[i].categroy.name,
            "price"         : super_foods[i].price,
            "stock"         : super_foods[i].stock_status,
            "sale_rate"     : super_foods[i].sale_rate.sale_rate} for i in range(len(super_foods))]

        return JsonResponse({"super_foods_list":super_foods_list}, status=200)

class LightFoodViews(View):
    def get(self,request):
        lightfoods = Categories.objects.get(name="Adult light Food")
        light_foods = Products.objects.filter(category_id =lightfoods)

        light_foods_list = [{
            "id"            : light_foods[i].id,
            "name"          : light_foods[i].name,
            "main_image"    : Images.objects.filter(product_id = light_foods[i].id).first().image_url,
            "sub_image"     : Images.objects.filter(product_id = light_foods[i].id).last().image_url,
            "category"      : light_foods[i].categroy.name,
            "price"         : light_foods[i].price,
            "stock"         : light_foods[i].stock_status,
            "sale_rate"     : light_foods[i].sale_rate.sale_rate} for i in range(len(light_foods))]

        return JsonResponse({"light_foods_list":light_foods_list}, status=200)







