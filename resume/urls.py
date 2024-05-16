from django.urls import path
from resume import views

urlpatterns = [
    path('list/', views.ResumeListAPIView.as_view(), name='resume-list'),
    path('create/', views.ResumeCreateAPIView.as_view(), name='resume-create'),
    path('detail/<int:pk>/', views.ResumeRetrieveAPIView.as_view(), name='resume-detail'),
    path('user/<int:user_id>/', views.ResumeByUserView.as_view(), name='resume-by-user'),
    path('update/<int:pk>/', views.ResumeUpdateAPIView.as_view(), name='resume-update'),
    path('delete/<int:pk>/', views.ResumeDestroyAPIView.as_view(), name='resume-delete'),
]