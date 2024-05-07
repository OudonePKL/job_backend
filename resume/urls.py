from django.urls import path
from .views import ResumeListCreateAPIView, ResumeRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', ResumeListCreateAPIView.as_view(), name='resume-list-create'),
    path('<int:pk>/', ResumeRetrieveUpdateDestroyAPIView.as_view(), name='resume-detail'),
]