import  json, re
import  bcrypt
import  jwt

from    django.http                 import  JsonResponse
from    django.views                import  View
from    boomdoggy.settings          import  SECRET_KEY

from    .models                     import  Users
import  validation
validate_phone = validation.validate_phone
validate_city = validation.validate_city



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
                return JsonResponse({'messages' : 'PLEASE_INSERT_YOUR_NAME'}, status = 400)

            if not re.match(REGEX_EMAIL, data['email']) : 
                return JsonResponse({'message' : 'INVALID_ID'}, status = 401)

            if not re.match(REGEX_PASSWORD, data['password']) : 
                return JsonResponse({'message' : 'INVALID_PASSWORD'}, status = 401)

            if Users.objects.filter(email = data['email']).exists() : 
                return JsonResponse({'message' : 'ALREADY_EXISTS'}, status = 401)

            else : 
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
                return JsonResponse({'message' : 'PASSWORD_IS_NOT_VALID'}, status = 400)
                    
            else :  
                return JsonResponse({'message' : "THIS_USER_DOES_NOT_EXIST"}, status = 401)

            
        except KeyError : 
            return JsonResponse({'message' : 'INVALID_KEY'}, status = 400)
