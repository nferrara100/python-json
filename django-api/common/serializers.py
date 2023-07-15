from common.models import FreeText
from rest_framework import serializers


class FreeTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeText
        fields = ["text"]
