from django.urls import path
from .import views

urlpatterns=[
    path('',views.Home),
    path('display',views.displayGrocery),
]