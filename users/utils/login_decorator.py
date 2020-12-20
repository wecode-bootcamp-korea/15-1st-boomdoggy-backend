from os import access
import  jwt
import  json

from    django.http         import JsonResponse
from    users.models        import Users
from    boomdoggy.settings  import SECRET_KEY

def login_check(func):
    def wrapper(self, request, *args, **kwargs):

        if "Authorization" not in request.headers:
            return JsonResponse({"message" : "INVALID_ACCESS"}, status=401)

        access_token = request.headers["Authorization"]

        try:
            data            = jwt.decode(access_token, SECRET_KEY, algorithms='HS256')
            user            = Users.objects.get(email = data.get('email'))
            request.user    = user

        except jwt.DecodeError:
            return JsonResponse({"message" : "INVALID_TOKEN"}, status=401)

        except Users.DoesNotExist:
            return JsonResponse({"message" : "INVALID_USER"}, status=401)

        return func(self, request, *args, **kwargs)
    
    return wrapper
