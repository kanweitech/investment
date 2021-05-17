from django.urls import path
from django.urls.conf import path, include
from .api.v1.views import api_home

app_name = "investments"

urlpatterns = [
    path('api/v1/', include(('investments.api.v1.urls', app_name), namespace="v1")),
    path("api-docs", api_home, name="api-home")
]