from rest_framework import generics, status, filters
from rest_framework.response import Response
from django.http import Http404
from .models import Resume
from .serializers import ResumeSerializer


class ResumeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["major", "skill"]  # Specify fields you want to search

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Resume created successfully."},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )


class ResumeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

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
            return Response({"message": "Resume updated successfully."})
        return Response(
            {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Resume updated partially."})
        return Response(
            {"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(
            {"message": "Resume deleted successfully."}, status=status.HTTP_200_OK
        )
