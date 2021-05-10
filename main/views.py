from django.shortcuts import render

from rest_framework import generics

from .serializers import InvestmentSerializer

from .models import Investments

# Create your views here.



class InvestmentList(generics.ListCreateAPIView):
	queryset = Investments.objects.all()
	serializer_class = InvestmentSerializer


class InvestmentDetail(generics.RetrieveDestroyAPIView):
	queryset = Investments.objects.all()
	serializer_class = InvestmentSerializer


