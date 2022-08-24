from django.shortcuts import render,get_object_or_404,redirect
from Store.models import Product
from Category.models import Category
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponse
def Store(request,category_slug=None):
    if (category_slug != None):# Only matching category and product is going to retrieve from Category and Product model
        categories=get_object_or_404(Category,slug=category_slug)
        products=Product.objects.filter(category=categories,is_available=True)
        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
        product_count = products.count()
    else:                       #He we are fetching all the products from product table
        products=Product.objects.all().filter(is_available=True)
        paginator=Paginator(products,3)
        page=request.GET.get('page')
        paged_product=paginator.get_page(page)
        product_count=products.count()
    return render(request,'Store.html',{'Prodct':paged_product,'pcount':product_count})
def product_detail(request,category_slug,product_slug):
    single_product=Product.objects.get(category__slug=category_slug,slug=product_slug)
    return render(request,'product_details.html',{'sproduct':single_product})
def Search(request):
    if request.method=='GET':
        vkeyword=request.GET.get('keyword')
        if vkeyword:
            products=Product.objects.order_by('-created_date').filter(Q(description__icontains=vkeyword) | Q(product_name__icontains=vkeyword))
        else:
            return redirect('store')
    return render(request,'Store.html',{'Prodct':products})
    #return HttpResponse(vkeyword)

