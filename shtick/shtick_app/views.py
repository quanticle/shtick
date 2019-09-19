from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello world, you've reached the index of the shtick app.")
