from django.urls import path
from . import views

urlpatterns = [
    path('', views.std_details),
    path('<int:pk>/', views.single_std),
]