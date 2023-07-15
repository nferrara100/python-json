from common.data import get_places
from common.models import FreeText
from common.serializers import FreeTextSerializer
from rest_framework import permissions, views, viewsets
from rest_framework.response import Response


# ViewSets define the view behavior.
class FreeTextViewSet(viewsets.ModelViewSet):
    queryset = FreeText.objects.all()
    serializer_class = FreeTextSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PlacesView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        spots = get_places(41.385128, 2.176872)
        return Response(spots)
