from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, Menu, MenuItem, Category
from django.contrib.auth.models import User
from .serializers import BookingSerializer, menuSerializer, UserSerializer, MenuItemSerializer,CategorySerializer
from rest_framework import viewsets
#from . import templates
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer=UserSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
        return Response({"status": "success", "data": serializer.data})
        return Response({"status": "error", "errors": serializer.errors})


def index(request):
    return render(request, 'index.html', {})

class CategoriesView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BookingView(generics.ListCreateAPIView):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer

    # def get(self, request):
    #     items=Booking.objects.all()
    #     serializer=bookingSerializer(items, many=True)
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer=bookingSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response({"status" : "success", "data":serializer.data})

class menuView(generics.ListCreateAPIView):
    items=Menu.objects.all()
    serializer=menuSerializer()

    def get(self, request):
        items=Menu.objects.all()
        serializer=menuSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=menuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"status" : "success", "data":serializer.data})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer