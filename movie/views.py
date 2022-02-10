from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse('<h1>Welcome to Home Page</h1><style>h1{color:blue}</style>')
    return render(request,'home.html')
# Create your views here.
