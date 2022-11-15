from django.urls import path, include
from rest_framework import routers
from common.views import FreeTextViewSet


router = routers.DefaultRouter()
router.register(r"free-text", FreeTextViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
