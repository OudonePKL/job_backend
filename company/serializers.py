from rest_framework import serializers
from .models import Company, CompanyRequest
from users.serializers import UserSerializer
from resume.serializers import ResumeSerializer


class OnlyCompanyInforSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        exclude = ["user"]


class CompanySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Company
        fields = "__all__"


class CompanyRequestSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    resume = ResumeSerializer()

    class Meta:
        model = CompanyRequest
        fields = "__all__"
