# views.py
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SMS
from .serializers import SMSSerializer

class SMSViewSet(viewsets.ModelViewSet):
    queryset = SMS.objects.all()
    serializer_class = SMSSerializer

# class SmsDetail(APIView):
#     def get(self,request):
#         obj = SMS.objects.all()
#         serializer = SMSSerializer(obj,many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self,request):
#         serializer = SMSSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


