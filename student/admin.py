from django.contrib import admin
from .models import Adress,Students

admin.site.register(Adress)
admin.site.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name',"age","adress")
    group_by = ('status')

