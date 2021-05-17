from django.urls import path

from .views import InvestmentList, InvestmentDetail

urlpatterns = [
	
	path("investment/", InvestmentList.as_view(), name="investment_list"),
	
	path("investment/<int:pk>/", InvestmentDetail.as_view(), name="investment_detail"),
]