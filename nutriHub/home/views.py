from django.shortcuts import render
import datetime
from django.http import HttpResponse
from fatsecret import Fatsecret

fs = Fatsecret('e66517406e33460995b087280ae6010d','1a74f2038c874aeda593adb0b2cd9dae')

def home(request):  
    return render(request, 'home.html',{})


def about(request):  
    return render(request, 'about.html',{})

def contact(request):  
    return render(request, 'contact.html',{})

def services(request):  
    return render(request, 'services.html',{})

def foodpage(request):  
    return render(request, 'foodpage.html',{})

def searchfood(request):  
    if request.method == 'GET':
        query = request.GET.get('food_query')
        if query:
            print(f"Query: {query}")
            results = fs.foods_search(query)
            # print(f"API Results: {results}")
            return render(request, 'foodpage.html', {'results': results,'query':query})
    return render(request, 'searchfood.html', {})

def recipes(request):  
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            results = fs.recipes_search(query)
            return render(request, 'food.html', {'results': results,'query':query})
    return render(request, 'recipes.html')

def food(request):  
    return render(request, 'food.html',{})
