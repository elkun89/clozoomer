from rest_framework import serializers
from myCloset.models import *

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        
class ApparelTypeSerializer(serializers.ModelSerializer): 
    class Meta:
        model = ApparelType
        
class ClothTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothType
        
class ShoesTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoesType

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location

class UserSerializer(serializers.ModelSerializer):
    apparels = serializers.ManyPrimaryKeyRelatedField()
    
    class Meta:
        model = User    
        
class ApparelInstanceSerializer(serializers.ModelSerializer):
    owner = serializers.Field(source='owner.username')
    class Meta:
        model = ApparelInstance