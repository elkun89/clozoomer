from rest_framework import serializers
from myCloset.models import *

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('name')
        
class ApparelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apparel
        
class ClothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cloth
        
class ShoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoes

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile