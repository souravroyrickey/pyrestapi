from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from .models import User
from . import serializer


# Create your views here.



class CreateUserView(generics.GenericAPIView):
    serializer_class = serializer.UserSerializer

    def post(self,request):
        data=request.data

        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UserView(generics.GenericAPIView):
    serializer_class = serializer.UserViewSerilizer

    def get(self,request):
        user=User.objects.all()
        serializer = self.serializer_class(instance=user, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
