import  json
from django.http.response import HttpResponseBadRequest

from    django.views                    import  View
from    django.db.models                import  Prefetch
from    django.http                     import  HttpRequest, JsonResponse

from    users.utils.login_decorator     import  login_check

from    .models                         import  Carts, Orders, Options
from    users.models                    import  Users
from    products.models                 import  Products, Images
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

    #장바구니 조회
    def get(self, request):
        user_id = 1

        try:
            order = Orders.objects.get(id=user_id)
            cart_list = order.carts_set.all()
            carts=[{
                "id": item.product_id,
                "product_name": item.product.name,
                "image": Images.objects.filter(product_id=item.product_id)[0].image_url,
                "option_kg": Carts.objects.filter(option_id=item.option_id)[0].option.kilogram,
                "price": item.product.price,
                "quantity": item.quantity,
                "total": int(item.product.price)*int(item.quantity)
                }for item in cart_list]
 
            return JsonResponse({'message' : 'SUCCESS', 'cart' : cart}, status=200)
        
        except Carts.DoesNotExist:
            return JsonResponse({'message' : 'SUCCESS', 'cart' : cart}, status=200)
