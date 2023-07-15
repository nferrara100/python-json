from common.views import FreeTextViewSet, PlacesView
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"free-text", FreeTextViewSet, basename="free-text")

urlpatterns = [
    path("places/", PlacesView.as_view(), name="places"),
    path("", include(router.urls)),
]
