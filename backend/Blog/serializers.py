from rest_framework import serializers
from .models import Blog_table, Comment_table

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment_table
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many = True, read_only = True)
    class Meta:
        model = Blog_table
        fields = '__all__'

