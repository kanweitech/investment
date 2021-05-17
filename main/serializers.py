from rest_framework import serializers

from .models import Investments



class InvestmentSerializer(serializers.ModelSerializer):
	roi = serializers.ReadOnlyField()

	
	class Meta:
		model = Investments
		# fields = '__all__'
		fields = ('uid', 'plan', 'amount', 'investor', 'phone', 'name', 'start', 'end', 'status', 'unit', 'address', 'fullname', 'roi')
	