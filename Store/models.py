from django.db import models
from Category.models import Category
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=200,unique=True)
    slug        =models.SlugField(max_length=200,unique=True)
    description =models.TextField(max_length=256)
    quantity    =models.IntegerField()
    category    =models.ForeignKey(Category,on_delete=models.CASCADE)
    images       =models.ImageField(upload_to='photos/product')
    price       =models.IntegerField()
    stock       =models.IntegerField()
    is_available=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now=True)
    modified_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name

    def get_url(self):
        return reverse('product_details', args=[self.category.slug,self.slug])

