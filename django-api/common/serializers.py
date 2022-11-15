from rest_framework import serializers
from common.models import FreeText


class FreeTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeText
        fields = ["text"]
