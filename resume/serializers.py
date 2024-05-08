from rest_framework import serializers
from .models import Resume
from users.serializers import UserSerializer


class ResumeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Resume
        fields = "__all__"


class ResumeCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = "__all__"

    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("Age cannot be negative.")
        return value
