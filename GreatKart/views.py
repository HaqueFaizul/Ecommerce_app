from django.shortcuts import render
from Store.models import Product
from django.core.paginator import Paginator

# Create your views here.
def Index(request):
    products=Product.objects.all().filter(is_available=True)
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
    return render(request,'Index.html',{'Products':paged_product })