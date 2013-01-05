from rest_framework import serializers
from myCloset.models import *

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        
class ApparelSerializer(serializers.ModelSerializer):
    owner = serializers.Field(source='owner.username')
    
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

class UserSerializer(serializers.ModelSerializer):
    apparels = serializers.ManyPrimaryKeyRelatedField()
    
    class Meta:
        model = User