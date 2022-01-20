from django.urls import path
from . import views

urlpatterns = [
    path('', views.mobileApiView.as_view()),
    path('/list/', views.mobileListApiView.as_view()),
    path('/create/', views.mobileCreateApiView.as_view()),
    path('/details/<pk>/', views.mobileDetailApiView.as_view()),
    path('/update/<pk>/', views.mobileUpdate.as_view()),
    path('/delete/<pk>/', views.mobileDelete.as_view()),

    path('/create_list/', views.mobileCreateListView.as_view()),
    path('/dud/<pk>/', views.mobileDUDApiView.as_view()),

    path('/lcapi/', views.mobileLCApiView.as_view()),
    path('/rudapi/<pk>/', views.mobileRUDApiView.as_view()),
]
