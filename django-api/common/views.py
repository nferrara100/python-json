from rest_framework import viewsets, permissions
from common.models import FreeText
from common.serializers import FreeTextSerializer


# ViewSets define the view behavior.
class FreeTextViewSet(viewsets.ModelViewSet):
    queryset = FreeText.objects.all()
    serializer_class = FreeTextSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
