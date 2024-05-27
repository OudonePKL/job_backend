from rest_framework import generics, status, filters
from rest_framework.response import Response
from django.http import Http404
from .models import Resume
from .serializers import ResumeSerializer, ResumeCreateUpdateSerializer
from django.shortcuts import get_object_or_404


class ResumeListAPIView(generics.ListAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["major", "skill"]  # Specify fields you want to search


class ResumeRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Resume not found"})


class ResumeByUserView(generics.RetrieveAPIView):
    serializer_class = ResumeSerializer

    def get(self, request, user_id, *args, **kwargs):
        try:
            resume = get_object_or_404(Resume, user_id=user_id)
            serializer = self.get_serializer(resume)

            return Response(
                {"message": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        except Http404:
            return Response(
                {"message": "No resume found for this user."},
                status=status.HTTP_404_NOT_FOUND,
            )


class ResumeCreateAPIView(generics.CreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeCreateUpdateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )


class ResumeUpdateAPIView(generics.UpdateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeCreateUpdateSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Resume not found"})

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "success", "data": serializer.data},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )


class ResumeDestroyAPIView(generics.DestroyAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeCreateUpdateSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Http404:
            raise Http404({"message": "Resume not found"})

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "success"}, status=status.HTTP_200_OK)
