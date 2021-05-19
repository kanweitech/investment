from decimal import Decimal
import decimal
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.response import Response
from rest_framework import generics, permissions, serializers, status, viewsets, mixins
from rest_framework.utils import json
from rest_framework.views import APIView
from .serailizers import InvestmentSerializer, SaveInvestmentSerializer
from acctmang.models import User
from investments.models import Investments, InvestmentPlan
from utils.generics import calculate_expected_returns

class InvestmentsViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):

    permission_classes = [permissions.AllowAny]
    serializer_class = InvestmentSerializer

    queryset = Investments.objects.all()


class CreateInvestmentAPI(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SaveInvestmentSerializer

    def post(self, request):

        serializer = SaveInvestmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data_bank= serializer.data
        plan_id = data_bank["plan_id"]
        email = data_bank["investor"]
        amount_invested = Decimal(data_bank["amount"])
        unit = data_bank["unit"]

        if unit < 1:
            return Response({
                "status": "failed",
                "message": "Unit cannot be less than 1"
            }, status=status.HTTP_406_NOT_ACCEPTABLE)


        if InvestmentPlan.objects.filter(plan_id=plan_id).count() > 0:
            plan = InvestmentPlan.objects.get(plan_id=plan_id)

            if amount_invested < Decimal("{:.2f}".format((plan.unit_amount * unit))):
                return Response({
                    "status": "failed",
                    "message": "Amount required for units not matched. A unit costs: {}".format(plan.unit_amount)
                }, status=status.HTTP_406_NOT_ACCEPTABLE)

            try:
                user = User.objects.get(email=email)

                # Generate ROI MetaData for User
                calc = calculate_expected_returns(amount_invested=amount_invested, roi_percentage=plan.roi_percentage)
                new_investment_metadata = {
                    "amount": amount_invested,
                    "current_roi_percentage": plan.roi_percentage,
                    "expected_capital_gain": calc["expected_capital_gain"],
                    "expected_return": calc["total_returns"]
                }

                Investments.objects.create(
                    investment_plan=plan,
                    amount=amount_invested,
                    user=user,
                    roi_metadata=json.dumps(new_investment_metadata, cls=DjangoJSONEncoder),
                    unit=unit
                )

                return Response({
                    "status": "success",
                    "message": "Investment created successfully",
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)
            except User.DoesNotExist:
                return Response({
                    "status": "failed",
                    "message": "Investor's email cannot be reconciled"
                }, status=status.HTTP_404_NOT_FOUND)

        else:
            return Response({
                "status": "failed",
                "message": "Invalid Plan ID"
            }, status=status.HTTP_404_NOT_FOUND)


