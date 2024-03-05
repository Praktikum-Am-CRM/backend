from rest_framework import serializers

from program.serializers import ProgramSerializer
from users.serializers import ManagerSerializer

from .models import Activity, Ambassador, AmbassadorStatus, Goal


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['id', 'goal_name', 'available']


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


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'activity_name', 'available']
