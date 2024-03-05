from rest_framework import serializers

from .models import Manager


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id', 'first_name', 'middle_name' 'last_name', 'email']
