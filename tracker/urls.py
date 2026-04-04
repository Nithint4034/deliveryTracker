from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tracker/', views.DeliveryListView.as_view(), name='delivery_list'),
    path('tracker/create/', views.DeliveryCreateView.as_view(), name='delivery_create'),
    path('tracker/<int:pk>/update/', views.DeliveryUpdateView.as_view(), name='delivery_update'),
    path('tracker/<int:pk>/delete/', views.DeliveryDeleteView.as_view(), name='delivery_delete'),
]