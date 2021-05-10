from rest_framework import serializers

from .models import Investments



class InvestmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Investments
		fields = '__all__'
