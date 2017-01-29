from django.shortcuts import render

from django.http import HttpResponse

def about(request):
    context_dict = {'name_message': "This tutorial has been put together by Dani Adkins"}
    return render(request, 'rango/about.html', context=context_dict)

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)



