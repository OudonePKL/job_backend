from django.conf.urls.static import static
from django.urls import path, include
from company import views

urlpatterns = [
    path("", views.CompanyList.as_view(), name='company-list'),
    path("orders/", views.OrderList.as_view(), name='orders-list'),
    path("order/create/", views.OrderCreate.as_view(), name='order-create'),
    path("order/update/<int:pk>/", views.OrderUpdate.as_view(), name='order-update'),
    path("order/detail/<int:pk>/", views.OrderDetail.as_view(), name='order-detail'),
    path("order/delete/<int:pk>/", views.OrderDelete.as_view(), name='order-delete'),
    
]