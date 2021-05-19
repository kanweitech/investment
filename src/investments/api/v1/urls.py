from django.urls import path
from .api import InvestmentsViewSet, CreateInvestmentAPI
from rest_framework import routers

router = routers.DefaultRouter()
router.register("investments", InvestmentsViewSet, "investments")

urlpatterns = [
    path("investments", CreateInvestmentAPI.as_view())
]
urlpatterns += router.urls