from django.shortcuts import render
from django.http import HttpResponse

#def home(request):
    #return HttpResponse('<h1>Welcome to Home Page</h1><style>h1{color:blue}</style>')
 #   return render(request,'home.html', {'name':'Jacobo Rave'})
# Create your views here.

def home(request):
    searchTerm = request.GET.get('searchMovie')
    return render(request,'home.html', {'searchTerm':searchTerm})


def about(request):
    return HttpResponse('<h1>Welcome to About page</h1>')
