from django.http import HttpResponse # HttpResponse is a class
# Create your views here.

def index (request):
    return HttpResponse("Hello, world. You're at the polls index.")

