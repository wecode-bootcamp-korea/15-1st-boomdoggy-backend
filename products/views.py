import json

from django.http    import JsonResponse
from django.views   import View

from products.models import Categories, Images, Products, Sale

class ProductListView(View):
    def get(self,request):
        category    = request.GET.get('name', None)
        products    = Products.objects.all()

        if category=="ourfoods":
            treats = Categories.objects.get(name="treats")
            foods = Products.objects.exclude(category_id = treats)

            foods_list = [{
                "id"            : foods[i].id,
                "name"          : foods[i].name,
                "main_image"    : Images.objects.filter(product_id = foods[i].id).first().image_url,
                "sub_image"     : Images.objects.filter(product_id = foods[i].id).last().image_url,
                "category"      : foods[i].category.name,
                "price"         : foods[i].price,
                "stock"         : foods[i].stock_status,
                "sale_rate"     : foods[i].sale_rate.sale_rate} for i in range(len(foods))]
            return JsonResponse({"ourfoods_list":foods_list}, status=200)

        else:
            category_id    = Categories.objects.get(name=category).id
            products    = Products.objects.filter(category_id=category_id)
            products_list   = f"{category}_list"

            products_list = [{
                "id"            : products[i].id,
                "name"          : products[i].name,
                "main_image"    : Images.objects.filter(product_id = products[i].id).first().image_url,
                "sub_image"     : Images.objects.filter(product_id = products[i].id).last().image_url,
                "category"      : products[i].category.name,
                "price"         : products[i].price,
                "stock"         : products[i].stock_status,
                "sale_rate"     : products[i].sale_rate.sale_rate} for i in range(len(products))]
            return JsonResponse({"products_list":products_list}, status=200)

