from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework import permissions
from myCloset.models import *
from myCloset.serializers import *

class BrandList(generics.ListCreateAPIView):
    model = Brand
    serializer_class = BrandSerializer
    
class ApparelList(generics.ListCreateAPIView):
    model = Apparel
    serializer_class = ApparelSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def pre_save(self, obj):
        obj.owner = self.request.user

class ClothList(generics.ListCreateAPIView):
    model = Cloth
    serializer_class = ClothSerializer

class ShoesList(generics.ListCreateAPIView):
    model = Shoes
    serializer_class = ShoesSerializer

class CategoryList(generics.ListCreateAPIView):
    model = Category
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserProfileList(generics.ListCreateAPIView):
    model = UserProfile
    serializer_class = UserProfileSerializer


class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Brand
    serializer_class = BrandSerializer

class ApparelDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Apparel
    serializer_class = ApparelSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def pre_save(self, obj):
        obj.owner = self.request.user
    
class ClothDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Cloth
    serializer_class = ClothSerializer
    
class ShoesDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Shoes
    serializer_class = ShoesSerializer
    
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Category
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    model = UserProfile
    serializer_class = UserProfileSerializer
    
class UserList(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer

class UserInstance(generics.RetrieveAPIView):
    model = User
    serializer_class = UserSerializer