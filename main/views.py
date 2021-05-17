from django.shortcuts import render

from rest_framework import generics

from .serializers import InvestmentSerializer

from .models import Investments

from rest_framework.permissions import IsAuthenticated

# Create your views here.



class InvestmentList(generics.ListCreateAPIView):
	queryset = Investments.objects.all()
	serializer_class = InvestmentSerializer
	# permission_classes = (IsAuthenticated,)


class InvestmentDetail(generics.RetrieveDestroyAPIView):
	queryset = Investments.objects.all()
	serializer_class = InvestmentSerializer
	# permission_classes = (IsAuthenticated,)


