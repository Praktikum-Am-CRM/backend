from rest_framework import serializers

from .models import Achieve


class AchieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achieve
        fields = ['id', 'achive_name', 'available']