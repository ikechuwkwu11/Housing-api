from django.core.serializers import serialize
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from.serializer import HouseSerializer, RegisterSerializer,LoginSerializer
from django.contrib.auth import authenticate,logout
from rest_framework import viewsets
from .models import House
# Create your views here.

class HouseView(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class Register(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"You have been registered.Now login"}, status=200)

class Login(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(name = serializer.data['name'], password = serializer.data['password'])
            return Response({"message":"You have been logged in"},status=200)
        return Response({"message":"Put in the right credentials"},status=400)

class Logout(APIView):
    def post(self,request):
        logout(request)
        return Response({'message':'You have been logged out'},status=200)

class AddHouse(APIView):
    def post(self,request):
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"House has been added","house": serializer.data} ,status=200)
        return Response({"message":"put in the right data"},status=400)


class EditHouse(APIView):
    def put(self,request,house_id):
        try:
            house = House.objects.get(id=house_id)
        except House.DoesNotExist:
            return Response({"error":"house does not exist"},status=400)

        serializer = HouseSerializer(house, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"House has been edited","house":serializer.data}, status=200)
        return Response({"message":"Hasn't been edited"},status=400)

class DeleteHouse(APIView):
    def delete(self,request,house_id):
        try:
            house = House.objects.get(id=house_id)
        except House.DoesNotExist:
            return Response({"error":"House is not found"},status=400)

        house.delete()
        return Response({"message":"House has been deleted"}, status = 200)




