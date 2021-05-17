from rest_framework.response import Response
from rest_framework import generics, permissions, status, viewsets
from .serailizers import InvestmentSerializer

from investments.models import Investments

class InvestmentsViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.AllowAny]
    serializer_class = InvestmentSerializer

    queryset = Investments.objects.all()