from rest_framework import serializers

from users.models import Manager


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = [
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'email',
            'username',
        ]
