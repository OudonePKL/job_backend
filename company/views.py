from django.shortcuts import render
from rest_framework import generics, status, filters
from .models import Company, Order, OrderItem, WebInfo
from .serializers import CompanySerializer, OrderSerializer, OrderCreateSerializer, WebInfoSerializer
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView


class CompanyList(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderCreate(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request):
        serializer = OrderCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderUpdate(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"message": "success", "data": serializer.data}, status=status.HTTP_200_OK)


class OrderDetail(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Order not found"})


class OrderDelete(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Order not found"})

    def delete(self, request, *args, **wkargs):
        instance = self.get_object()
        instance.delete()
        return Response(
            {"message": "success"}, status=status.HTTP_200_OK
        )


class WebInfoListCreate(generics.ListAPIView):
    queryset = WebInfo.objects.all()
    serializer_class = WebInfoSerializer

# class WebInfoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = WebInfo.objects.all()
#     serializer_class = WebInfoSerializer

class WebInfoCreateOrUpdate(APIView):

    def post(self, request, *args, **kwargs):
        try:
            # Assuming there's only one instance of WebInfo to update
            webinfo = WebInfo.objects.first()
            if webinfo:
                serializer = WebInfoSerializer(webinfo, data=request.data)
            else:
                serializer = WebInfoSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)