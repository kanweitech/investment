from django.urls import path
from .api import InvestmentsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register("investments", InvestmentsViewSet, "investments")

urlpatterns = []
urlpatterns += router.urls