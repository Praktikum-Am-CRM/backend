from datetime import datetime

from django.db.models import Q
from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from achievements.models import Achieve
from achievements.serializers import AchieveSerializer
from crm_settings.crm_setting import crm_settings
from program.models import Program
from program.serializers import ProgramSerializer
from telegram.models import TelegramBot
from telegram.serializers import TelegramBotSerializer

from .models import (
    Activity,
    Ambassador,
    AmbassadorAchieve,
    AmbassadorActivity,
    AmbassadorGoal,
    AmbassadorProgram,
    AmbassadorStatus,
    Goal,
)


def set_programs(ambassador, programs_id):
    ambassador.programs.clear()
    programs = Program.objects.filter(id__in=programs_id)
    ambassador_programs = []
    for program in programs:
        ambassador_program = AmbassadorProgram(
            ambassador=ambassador, program=program
        )
        ambassador_programs.append(ambassador_program)
    AmbassadorProgram.objects.bulk_create(ambassador_programs)


def set_goals(ambassador, goals_id, ambassador_own_version=''):
    ambassador.goals.clear()
    goals = Goal.objects.filter(id__in=goals_id)
    ambassador_goals = []
    for goal in goals:
        own_version = (
            ambassador_own_version
            if (goal.id == crm_settings.goal_own_version.id)
            else ''
        )
        ambassador_goal = AmbassadorGoal(
            ambassador=ambassador,
            goal=goal,
            own_version=own_version,
        )
        ambassador_goals.append(ambassador_goal)
    AmbassadorGoal.objects.bulk_create(ambassador_goals)


def set_activity(ambassador, activity_id):
    ambassador.activity.clear()
    activities = Activity.objects.filter(id__in=activity_id)
    ambassador_activities = []
    for activity in activities:
        ambassador_activity = AmbassadorActivity(
            ambassador=ambassador,
            activity=activity,
        )
        ambassador_activities.append(ambassador_activity)
    AmbassadorActivity.objects.bulk_create(ambassador_activities)


def set_achieve(ambassador, achieves_id):
    achieves = Achieve.objects.filter(id__in=achieves_id)
    ambassador_achieves = []
    for achieve in achieves:
        achieve_available = AmbassadorAchieve.objects.filter(
            Q(achieve=achieve) & Q(ambassador=ambassador)
        )
        assigment_data = (
            achieve_available[0].assignment_date
            if (achieve_available)
            else datetime.now().date()
        )
        ambassador_activity = AmbassadorAchieve(
            ambassador=ambassador,
            achieve=achieve,
            assignment_date=assigment_data,
        )
        ambassador_achieves.append(ambassador_activity)
    ambassador.achieves.clear()
    AmbassadorAchieve.objects.bulk_create(ambassador_achieves)


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['id', 'goal_name', 'available']


class AmbassadorGoalSerializer(serializers.ModelSerializer):
    goal = GoalSerializer()

    class Meta:
        model = AmbassadorGoal
        fields = [
            'goal',
            'own_version',
        ]


class AmbassadorStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmbassadorStatus
        fields = ['id', 'status_name', 'sort_level', 'available']


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'activity_name', 'available']


class AmbassadorSerializer(serializers.ModelSerializer):
    goals = serializers.SerializerMethodField(method_name='get_goals')
    activity = ActivitySerializer(many=True)
    programs = ProgramSerializer(many=True)
    telegram_bot = TelegramBotSerializer()
    achieves = AchieveSerializer(many=True)
    status = AmbassadorStatusSerializer()

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

    def get_goals(self, obj):
        ambassador_goals = AmbassadorGoal.objects.filter(
            ambassador=obj,
        )
        ambassador_goals_ser = AmbassadorGoalSerializer(
            ambassador_goals, many=True
        )
        return ambassador_goals_ser.data


class AmbassadorShortSerializer(serializers.ModelSerializer):
    status = AmbassadorStatusSerializer()

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


class AmbassadorUpdateSerializer(serializers.ModelSerializer):
    programs = serializers.ListSerializer(
        child=serializers.UUIDField(),
        required=True,
    )
    goals = serializers.UUIDField()
    activity = serializers.ListSerializer(
        child=serializers.UUIDField(),
        required=False,
    )
    achieves = serializers.ListSerializer(
        child=serializers.UUIDField(),
        required=False,
    )
    own_version = serializers.CharField(
        max_length=250,
        required=False,
    )

    class Meta:
        model = Ambassador
        fields = [
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
            'own_version',
        ]

    def update(self, instance, validated_data):
        programs_id = validated_data.pop('programs', None)
        goals_id = validated_data.pop('goals', None)
        activity_id = validated_data.pop('activity', None)
        achieve_id = validated_data.pop('achieves', None)
        own_version = validated_data.pop('own_version', '')

        if programs_id:
            set_programs(instance, programs_id)
        if goals_id:
            set_goals(instance, [goals_id], own_version)
        if activity_id:
            set_activity(instance, activity_id)
        if achieve_id:
            set_achieve(instance, achieve_id)

        return super().update(instance, validated_data)


class AmbassadorBotCreateSerializer(serializers.Serializer):
    telegram_id = serializers.CharField(max_length=100, required=True)
    first_name = serializers.CharField(max_length=50, required=True)
    last_name = serializers.CharField(max_length=50, required=True)
    middle_name = serializers.CharField(max_length=50, required=False)
    gender = serializers.CharField(max_length=50, required=True)
    birthday = serializers.DateField()
    programs = serializers.ListSerializer(
        child=serializers.UUIDField(),
        required=True,
    )
    goal = serializers.UUIDField()
    phone = serializers.CharField(max_length=20, required=False)
    email = serializers.EmailField()
    size_clothing = serializers.CharField(max_length=2, required=False)
    size_choe = serializers.IntegerField(default=0, required=False)
    address_index = serializers.CharField(max_length=10, required=False)
    address_country = serializers.CharField(max_length=50, required=True)
    address_region = serializers.CharField(max_length=50, required=False)
    address_district = serializers.CharField(max_length=50, required=False)
    address_settlement = serializers.CharField(max_length=50, required=True)
    address_street = serializers.CharField(max_length=50, required=False)
    address_house = serializers.IntegerField(min_value=0, required=False)
    address_building = serializers.CharField(max_length=10, required=False)
    address_apartment = serializers.CharField(max_length=10, required=False)
    promocode = serializers.CharField(max_length=255, required=False)
    own_version = serializers.CharField(
        max_length=250,
        required=False,
    )

    def create(self, validated_data):
        telegram_id = validated_data.pop('telegram_id')
        programs_id = validated_data.pop('programs')
        goal_id = validated_data.pop('goal')
        activity_id = validated_data.pop('activity', None)
        achieve_id = validated_data.pop('achieves', None)
        own_version = validated_data.pop('own_version', '')

        telegram_user = get_object_or_404(TelegramBot, telegram_id=telegram_id)
        if telegram_user.ambassadors.exists():
            ambassador = telegram_user.ambassadors.first()
            set_programs(ambassador, programs_id)
            set_goals(ambassador, [goal_id], own_version)
            if activity_id:
                set_activity(ambassador, activity_id)
            if achieve_id:
                set_achieve(ambassador, achieve_id)

            ambassador_serializer = AmbassadorUpdateSerializer(
                ambassador, data=validated_data, partial=True
            )
            ambassador_serializer.is_valid(raise_exception=True)
            ambassador_serializer.save()

        else:
            ambassador = Ambassador.objects.create(
                telegram_bot=telegram_user,
                status=crm_settings.default_ambassador_status,
                **validated_data,
            )
            set_programs(ambassador, programs_id)
            set_goals(ambassador, [goal_id], own_version)

        return ambassador

    def to_representation(self, instance):
        serializer = AmbassadorSerializer(
            instance,
            context={'request': self.context.get('request')},
        )
        return serializer.data
