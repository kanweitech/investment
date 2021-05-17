from django.db import models
from django.db.models import fields
from rest_framework import serializers
from investments.models import Investments

class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investments
        fields = ("amount", "roi", "unit")
