from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response
from .models import Product
from .serializer import ProductSerializer


# Create your views here.
class ProductsListApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class RetrieveProduct(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"


class CreateProductAPIView(CreateAPIView):
    def post(self, request):

        try:
            Product.objects.create(
                name=request.data.get("name"),
                description=request.data.get("description"),
            )
        except Exception as e:
            return Response("", 500)
        return Response("", 200)
