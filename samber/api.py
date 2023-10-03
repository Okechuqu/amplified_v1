from ninja import NinjaAPI, Schema

api = NinjaAPI()

@api.get('/home')
def func(request, name='Emma'):
    return f"Hello {name}"

@api.get('/calc')
def math(request, a:int, b:int):
    return{"add": a + b, "multiply": a*b }

class MyApi(Schema):
    name: str = "This is my first api"

@api.post('/index')
def hello(request, data:MyApi):
    return f"How is {data.name}"

class UserSchema(Schema):
    username: str
    is_authenticated: bool 
    email: str = None
    first_name: str =None
    last_name: str = None
 
class Error(Schema):
    message: str

@api.get('/info', response={200: UserSchema, 403: Error})
def info(request):
    if not request.user.is_authenticated:
        return 403, {'message': 'Please sign in'}
    return request.user
