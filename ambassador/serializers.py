from rest_framework import serializers

from achievements.serializers import AchieveSerializer
from program.serializers import ProgramSerializer
from telegram.serializers import TelegramBotSerializer

from .models import Activity, Ambassador, AmbassadorStatus, Goal


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['id', 'goal_name', 'available']


class AmbassadorStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmbassadorStatus
        fields = ['id', 'status_name', 'sort_level', 'available']


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'activity_name', 'available']


class AmbassadorSerializer(serializers.ModelSerializer):
    goals = GoalSerializer(many=True)
    activity = ActivitySerializer(many=True)
    programs = ProgramSerializer(many=True)
    telegram_bot = TelegramBotSerializer()
    achieves = AchieveSerializer(many=True)

    class Meta:
        model = Ambassador
        fields = [
            'id',
            'telegram_bot',
            'status',
            'manager',
            'promocode',
            'receipt_date',
            'reminder_counter',
            'address_country',
            'address_index',
            'address_region',
            'address_district',
            'address_settlement',
            'address_street',
            'address_house',
            'address_building',
            'address_apartment',
            'size_clothing',
            'size_choe',
            'email',
            'note',
            'blog_link',
            'place_work',
            'specialty_work',
            'educational_institution',
            'first_name',
            'last_name',
            'middle_name',
            'gender',
            'birthday',
            'programs',
            'goals',
            'activity',
            'achieves',
            'phone',
        ]


class AmbassadorShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambassador
        fields = [
            'id',
            'status',
            'manager',
            'promocode',
            'receipt_date',
            'reminder_counter',
            'email',
            'first_name',
            'last_name',
            'middle_name',
            'gender',
            'birthday',
            'phone',
            'size_clothing',
            'size_choe',
            'note',
        ]
