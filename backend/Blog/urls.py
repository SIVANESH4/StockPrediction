from django.urls import path
from . import views

urlpatterns = [
    path('blog/',views.BlogView.as_view()),
    path('comments/',views.CommentView.as_view()),
    path('blog/<int:pk>/', views.BlogDetailView.as_view()),
    path('comments/<int:pk>/',views.CommentDetailView.as_view())
]