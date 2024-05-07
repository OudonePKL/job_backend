from rest_framework import serializers
from .models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'

    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("Age cannot be negative.")
        return value
