from django.conf.urls.static import static
from django.urls import path, include
from company import views

urlpatterns = [
    path("", views.CompanyList.as_view(), name='company-list'),
    path("request/", views.CompanyRequestList.as_view(), name='company-request-list'),
]