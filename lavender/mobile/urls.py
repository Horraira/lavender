from django.urls import path

from . import views

urlpatterns = [
    path('', views.Mobiles.as_view(), name='Mobile List'),
    path('mobile_details/<pk>/', views.MobileDetails.as_view(), name='mobile_details'),
    path('addMobile/', views.AddMobile.as_view(), name='addMobile'),
    path('delete_mobile/<pk>/', views.DeleteMobile, name='delete_mobile'),
]
