from rest_framework import serializers
from .models import Company, Order, OrderItem, WebInfo
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


class OrderItemSerializer(serializers.ModelSerializer):
    resume = ResumeSerializer()

    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = [
            "resume",
        ]


class OrderSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    def get_items(self, obj):
        order_items = OrderItem.objects.filter(order=obj)
        serializer = OrderItemSerializer(order_items, many=True)
        return serializer.data

    class Meta:
        model = Order
        fields = ["id", "company", "description", "items", "status", "created_at"]


class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderItemCreateSerializer(many=True, write_only=True)

    def create(self, validated_data):
        order_items_data = validated_data.pop("items")
        order = Order.objects.create(**validated_data)
        for order_item_data in order_items_data:
            OrderItem.objects.create(order=order, **order_item_data)
        return order

    class Meta:
        model = Order
        fields = ["company", "description", "items"]


class WebInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = WebInfo
        fields = "__all__"
