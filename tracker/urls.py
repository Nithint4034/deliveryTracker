from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tracker/', views.DeliveryListView.as_view(), name='delivery_list'),
    path('tracker/create/', views.DeliveryCreateView.as_view(), name='delivery_create'),
    path('tracker/<int:pk>/update/', views.DeliveryUpdateView.as_view(), name='delivery_update'),
    path('tracker/<int:pk>/delete/', views.DeliveryDeleteView.as_view(), name='delivery_delete'),
    path('tracker-2/', views.SecondaryDeliveryListView.as_view(), name='secondary_delivery_list'),
    path('tracker-2/create/', views.SecondaryDeliveryCreateView.as_view(), name='secondary_delivery_create'),
    path('tracker-2/<int:pk>/update/', views.SecondaryDeliveryUpdateView.as_view(), name='secondary_delivery_update'),
    path('tracker-2/<int:pk>/delete/', views.SecondaryDeliveryDeleteView.as_view(), name='secondary_delivery_delete'),
]