from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('api/v1/students/', include('students.urls')),
    path('api/v1/employees/', include('employee.urls')),
    path('api/v1/blogs/', include('Blog.urls')),
    path('api/v1/corporate/', include('Corporate.urls')),
]
