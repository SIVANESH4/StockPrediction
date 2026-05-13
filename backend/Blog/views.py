from django.shortcuts import render
from rest_framework import generics
from .models import Blog_table, Comment_table
from .serializers import BlogSerializer, CommentSerializer
# Create your views here.
class BlogView(generics.ListCreateAPIView):
    queryset = Blog_table.objects.all()
    serializer_class = BlogSerializer

class CommentView(generics.ListCreateAPIView):
    queryset = Comment_table.objects.all()
    serializer_class = CommentSerializer

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment_table.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog_table.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'
