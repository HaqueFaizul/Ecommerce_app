from django.shortcuts import render
from .models import Grocery

# Create your views here.

def Home(request):
    return render(request,"HomePage.html")
def displayGrocery(request):
    gobj=Grocery.objects.all()
    return render(request,'DisplayGrocery.html',{'grocery':gobj})
