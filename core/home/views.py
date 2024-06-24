from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):


    peoples = [
        {'name':'Randhir Kumar', 'age':23},
        {'name':'Saurabh Kumar', 'age':24},
        {'name':'Pritam Arya', 'age':25},
        {'name':'Ritesh Modi', 'age':21},
        {'name':'Piyush Sharma', 'age':23},
    ]

    return render(request, "home/index.html", context={'peoples':peoples, 'page':'home'})

    # return render(request, "index.html")
    # return HttpResponse("<h1>Hey, I am a Django Server</h1>")
    # We can use """ """ to insert multiple HTML elements
# return HttpResponse("""<h1>Hey, I am a Django Server</h1>
    # <p> Hey this is coming from Django server </p>
    # <hr>
    # <h3 style="color: red"> Hope you are loving it </h3>  
# """)

def about(request):
    context = {'page' : 'About'}
    return render(request,"home/about.html",context)

def contact(request):
    context = {'page' : 'Contact'}
    return render(request,"home/contact.html",context)

def success_page(request):
    return HttpResponse("Hey, This is a success Page")
