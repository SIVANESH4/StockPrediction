from django.contrib import admin
from .models import Emp_table
# Register your models here.
class list_view(admin.ModelAdmin):
    list_display = ('e_id','e_name')

admin.site.register(Emp_table, list_view)