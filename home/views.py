from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def game(request):
    return render(request, "game.html")

def login(request):
    return render(request, "login.html")

def contact(request):
    return render(request, "contact.html")

def profile(request):
    return render(request, "profile.html")

def signup(request):
    return render(request,"signup.html")
