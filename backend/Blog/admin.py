from django.contrib import admin
from .models import Blog_table, Comment_table
# Register your models here.

admin.site.register(Blog_table)
admin.site.register(Comment_table)