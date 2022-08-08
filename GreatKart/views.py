from django.shortcuts import render
from Store.models import Product

# Create your views here.
def Index(request):
    products=Product.objects.all().filter(is_available=True)
    return render(request,'Index.html',{'Products':products})