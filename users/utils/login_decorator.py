import  jwt, json

from    django.http             import JsonResponse
from    django.core.exceptions  import ObjectDoesNotExist

from    users.models            import Users
from    boomdoggy.settings      import SECRET_KEY

def login_check(func):
    def wrapper(self, request, *args, **kwargs):

        try:
            access_token    =   request.headers.get('Authorization', None)
            payload         =   jwt.decode(access_token, SECRET_KEY, algorithms='HS256')
            user            =   Users.objects.get(email=payload['email'])
            request.user    =   user
            
            return func(self, request, *args, **kwargs)
        
        except Users.DoesNotExist:
            return JsonResponse({"message" : "INVALID_USER"}, status=400)

        except jwt.exceptions.DecodeError:
            return JsonResponse({'message' : 'INVALID_TOKEN'}, status=400)

        return func(self, request, *args, **kwargs)

    return wrapper
