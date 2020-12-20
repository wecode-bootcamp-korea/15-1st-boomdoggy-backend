import json

from django.http    import JsonResponse
from django.views   import View

from products.models import Categories, Images, Products

class TreatView(View):
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
