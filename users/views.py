import  json, re
import  bcrypt
import  jwt

from    django.http                 import  JsonResponse
from    django.views                import  View
from    boomdoggy.settings          import  SECRET_KEY

from    .models                     import  Users, AddressList
from    users.utils                 import  login_decorator


class SignUp(View) : 
    def post(self, request) : 
        data = json.loads(request.body)

        #비밀번호 암호화
        hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        
        #이메일, 비밀번호 유효성
        REGEX_EMAIL         = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        REGEX_PASSWORD      = '^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,16}$'

        try : 
            if not (data['first_name'] and data['last_name']) : 
                return JsonResponse({'messages' : 'INVALID_NAME'}, status = 400)

            if not re.match(REGEX_EMAIL, data['email']) : 
                return JsonResponse({'message' : 'INVALID_EMAIL'}, status = 400)

            if not re.match(REGEX_PASSWORD, data['password']) : 
                return JsonResponse({'message' : 'INVALID_PASSWORD'}, status = 400)

            if Users.objects.filter(email = data['email']).exists() : 
                return JsonResponse({'message' : 'ALREADY_EXISTS'}, status = 401)

            Users.objects.create(
                    first_name  =   data['first_name'],
                    last_name   =   data['last_name'],
                    email       =   data['email'],
                    password    =   hashed_password.decode('utf-8'),
                    )
            return JsonResponse({'message' : 'SUCCESS'}, status = 201)

        except KeyError : 
            return JsonResponse({'message' : 'INVALID_KEY'}, status = 400)


class SignIn(View) : 

    def post(self, request) : 
        data        = json.loads(request.body)
        email       = data.get('email')
        password    = data.get('password')

        
        try : 
            if Users.objects.filter(email = email).exists() : 
                user = Users.objects.get(email = email)

                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')) : 
                    access_token = jwt.encode(
                            {'email': email}, SECRET_KEY, algorithm = 'HS256'
                            ).decode('utf-8')

                    return JsonResponse({'message' : 'SUCCESS', 'Token' : access_token}, status = 200)
                return JsonResponse({'message' : 'INVALID_PASSWORD'}, status = 401) 
            return JsonResponse({'message' : "INVALID_USER"}, status = 401)

        except KeyError : 
            return JsonResponse({'message' : 'INVALID_KEY'}, status = 400) 


class Address(View):
    @login_decorator.login_check
    def post(self, request):
        data                = json.loads(request.body)
        
        try:
            if not (
                    data['first_name'] and data['last_name'] and data['address'] and data['city'] and 
                    data['country_region'] and data['postcode'] and data['phone_number']
                    ):
                return JsonResponse({'message' : 'INVALID_ADDRESS'}, status = 401)

            else:
                user_id = data['user_id']
                AddressList.objects.create(
                        first_name          =   data['first_name'],
                        last_name           =   data['last_name'],
                        address             =   data['address'],
                        appartment_type     =   data['appartment_type'],
                        city                =   data['city'],
                        country_region      =   data['country_region'],
                        postcode            =   data['postcode'],
                        phone_number        =   data['phone_number'],
                        company             =   data['company'],
                        user                =   Users.objects.filter(id=user_id).get()
                        )
                return JsonResponse({'message' : 'SUCCESS'}, status = 201)
            

        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEY'}, status = 400)

    def delete(self, request):
        address = AddressList.objects.get(id=address_list_id)
        address.delete()
