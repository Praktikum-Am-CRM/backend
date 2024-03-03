from rest_framework import serializers

from .models import Ambassador, AmbassadorStatus, Manager


class ManagerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = "__all__"


class AmbassadorStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = AmbassadorStatus
        fields = "__all__"


class AmbassadorSerialisers(serializers.ModelSerializer):
    status = AmbassadorStatusSerializers(read_only=True)
    manager = ManagerSerializers(read_only=True)

    class Meta:
        model = Ambassador
        fields = "__all__"
