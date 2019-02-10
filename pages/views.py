from django.shortcuts import render

def home(request):
    jorts = "Jorts are the most fashionable pant"
    return render(request, "home.html", {"joorts": jorts})


def about(request):
    my_name = "Hello, My name is Hunter Holm"
    return render(request, "about.html", {"name": my_name})

def index(request):
    return render(request, "index.html")


