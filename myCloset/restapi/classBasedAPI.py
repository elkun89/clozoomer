from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework import permissions
from myCloset.models import *
from myCloset.restapi.serializers import *

#===============================================================================
# List block
#===============================================================================
class BrandList(generics.ListCreateAPIView):
    model = Brand
    serializer_class = BrandSerializer
    
class ApparelTypeList(generics.ListCreateAPIView):
    model = ApparelType
    serializer_class = ApparelTypeSerializer
        
class ApparelInstanceList(generics.ListCreateAPIView):
    model = ApparelInstance
    serializer_class = ApparelInstanceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def pre_save(self, obj):
        obj.owner = self.request.user

class ClothTypeList(generics.ListCreateAPIView):
    model = ClothType
    serializer_class = ClothTypeSerializer

class ShoesTypeList(generics.ListCreateAPIView):
    model = ShoesType
    serializer_class = ShoesTypeSerializer

class CategoryList(generics.ListCreateAPIView):
    model = Category
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserProfileList(generics.ListCreateAPIView):
    model = UserProfile
    serializer_class = UserProfileSerializer
    
class LocationList(generics.ListCreateAPIView):
    model = Location
    serializer_class = LocationSerializer

#===============================================================================
# Detail block
#===============================================================================
class BrandDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Brand
    serializer_class = BrandSerializer

class ApparelTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    model = ApparelType
    serializer_class = ApparelTypeSerializer
        
class ApparelInstanceDetail(generics.RetrieveUpdateDestroyAPIView):
    model = ApparelInstance
    serializer_class = ApparelInstanceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
    def pre_save(self, obj):
        obj.owner = self.request.user
    
class ClothDetail(generics.RetrieveUpdateDestroyAPIView):
    model = ClothType
    serializer_class = ClothTypeSerializer
    
class ShoesDetail(generics.RetrieveUpdateDestroyAPIView):
    model = ShoesType
    serializer_class = ShoesTypeSerializer
    
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
    
class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Location
    serializer_class = LocationSerializer