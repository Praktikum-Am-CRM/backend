from rest_framework import serializers

from program.serializers import ProgramSerializer
from users.serializers import ManagerSerializer

from .models import Ambassador, AmbassadorStatus


class AmbassadorStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmbassadorStatus
        fields = "__all__"


class AmbassadorSerializer(serializers.ModelSerializer):
    status = AmbassadorStatusSerializer(read_only=True)
    manager = ManagerSerializer(read_only=True)
    program = ProgramSerializer(read_only=True)

    class Meta:
        model = Ambassador
        fields = "__all__"
