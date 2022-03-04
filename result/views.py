from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from . import serializer
from django.shortcuts import get_object_or_404
from .models import Result
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# Create your views here.
class ResultView(generics.GenericAPIView):
    serializer_class = serializer.ResultDetailSerializer
    queryset = Result.objects.all()
    #Token Authenticaion
    permission_classes = [IsAuthenticated]
    authentication_classes =[TokenAuthentication]

    def get(self, request):
        results = Result.objects.all()
        serializer = self.serializer_class(instance=results, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        data=request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ResultSearchView(generics.GenericAPIView):
    serializer_class = serializer.ResultDetailSerializer
    queryset = Result.objects.all()
    def get(self,request,rollnum):
        results = get_object_or_404(Result, rollnumber=rollnum)
        serializer = self.serializer_class(instance=results)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

class ResultDetailView(generics.GenericAPIView):
    serializer_class = serializer.ResultDetailSerializer
    queryset = Result.objects.all()
    # Token Authenticaion
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def put(self,request,rollnum):
        data = request.data
        result = get_object_or_404(Result, rollnumber=rollnum)
        serializer = self.serializer_class(data=data, instance=result)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,rollnum):
        result = get_object_or_404(Result, rollnumber=rollnum)
        result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UpdateGradeView(generics.GenericAPIView):
    serializer_class = serializer.UpdateGradeSerializer
    queryset = Result.objects.all()
    # Token Authenticaion
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def put(self,request,rollnum):
        data = request.data
        result = get_object_or_404(Result, rollnumber=rollnum)
        if data=='F':
            result.resultStatus='FAIL'
        else:
            result.resultStatus = 'PASS'
        result.save()
        serializer = self.serializer_class(instance=result,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

