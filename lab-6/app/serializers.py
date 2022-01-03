from app.models import Disk
from rest_framework import serializers


class DiskSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Disk
        # Поля, которые мы сериализуем
        fields = ["id", "title", "size", "format", "description"]