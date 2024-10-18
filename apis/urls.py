from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", ProductsListApiView.as_view()),
    path("<str:id>", RetrieveProduct.as_view()),
    path("register/", CreateProductAPIView.as_view()),
]
