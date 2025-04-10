from rest_framework import serializers
from.models import User,House

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['name','password','email']

    def create(self, validat_data):
        return User.objects.create(**validat_data)

class LoginSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    password = serializers.CharField()
    class Meta:
        model = User
        fields = ['name', 'password']
