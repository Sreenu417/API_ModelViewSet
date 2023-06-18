from django.shortcuts import render

# Create your views here.
from app.models import *
from app.serializers import *
from rest_framework import viewsets

class ProductcrudMVS(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer