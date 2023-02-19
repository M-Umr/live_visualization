#from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello, Django!")
    print('this is print in views.py')
    print(request)
    return render(request, 'index.html')