from django.shortcuts import render
from rest_framework import generics, status, filters
from .models import Company, CompanyRequest
from .serializers import CompanySerializer, CompanyRequestSerializer


class CompanyList(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    

class CompanyRequestList(generics.ListAPIView):
    queryset = CompanyRequest.objects.all()
    serializer_class = CompanyRequestSerializer
    
        
