from django.urls import path
from . import views

urlpatterns = [
    path('', views.DeliveryListView.as_view(), name='delivery_list'),
    path('create/', views.DeliveryCreateView.as_view(), name='delivery_create'),
    path('<int:pk>/update/', views.DeliveryUpdateView.as_view(), name='delivery_update'),
    path('<int:pk>/delete/', views.DeliveryDeleteView.as_view(), name='delivery_delete'),
]