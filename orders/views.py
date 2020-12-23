import  json
from django.http.response import HttpResponseBadRequest

from    django.views                    import  View
from    django.db.models                import  Prefetch
from    django.http                     import  HttpRequest, JsonResponse

from    users.utils.login_decorator     import  login_check

from    .models                         import  Carts, Orders, Options
from    users.models                    import  Users
from    products.models                 import  Products
from    payments.models                 import  PaymentsType



class Cart(View):
#    @login_check
    def post(self, request): #카트 상품 넣기
        try:
            data = json.loads(request.body)
            user_id = 1

            if not Orders.objects.filter(user_id=user_id, order_status_id=1).exists():

                add_order = Orders.objects.create(
                        user_id             = user_id,
                        order_status_id     = 1,
                        payment_id          = 1,
            )

                add_order_id = add_order.id

            else:
                add_order_id = Orders.objects.get(user_id=user_id, order_status_id=1).id

            if Carts.objects.filter(order_id=add_order_id, product_id=data['product_id']).exists():
                cart    = Carts.objects.get(order_id=add_order_id, product_id=data['product_id'])
                cart.quantity += int(data['quantity'])
                cart.total_price = cart.product.price * int(cart.quantity)
                cart.save()

                return JsonResponse({'message' : 'SUCCESS'}, status=200)
            
            Carts.objects.create(
                    order_id            = add_order_id,
                    product_id          = data['product_id'],
                    quantity            = data['quantity'],
                    option_id           = data['option_id'],
                    payments_type_id    = data['payments_type_id'],
                    total_price         = int(data['quantity']) * int(Products.objects.filter(id=data['product_id']).values_list('price', flat=True)[0]),
                    )

            return JsonResponse({'message' : 'SUCCESS'}, status = 201)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)
