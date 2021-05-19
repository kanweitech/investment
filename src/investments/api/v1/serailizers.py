from decimal import Decimal
from django.core.validators import MinValueValidator
from rest_framework import serializers
from investments.models import Investments

class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investments
        fields = "__all__"

class SaveInvestmentSerializer(serializers.Serializer):
    plan_id = serializers.UUIDField()
    amount = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[
            MinValueValidator(Decimal("0.00")),
        ],
    )
    investor = serializers.EmailField()
    unit = serializers.IntegerField()