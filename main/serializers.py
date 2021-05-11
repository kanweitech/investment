from rest_framework import serializers

from .models import Investments



class InvestmentSerializer(serializers.ModelSerializer):

	
	class Meta:
		model = Investments
		# fields = '__all__'
		fields = ('uid', 'plan', 'amount', 'investor', 'phone', 'name', 'end', 'roi', 'status', 'unit', 'address', 'fullname')
	