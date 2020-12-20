import json

from django.http    import JsonResponse
from django.views   import View

from products.models import Categories, Images, Products

class TreatView(View):
    def get(self,request):
        products    = Products.objects.all()
        products    = Products.objects.filter(category_id = treats)


        treats_query    = products.filter(category_id = treats)



        return JsonResponse({"treats_list" : treats_list}, status=200)


