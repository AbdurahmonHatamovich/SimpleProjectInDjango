from django.contrib import admin
from .models import Adress, Students

admin.site.register(Adress)

@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'get_address_name')

    def get_address_name(self, obj):
        return obj.address.name if obj.address else "-"  # Assuming 'name' is a field in the Address model

    get_address_name.short_description = 'Address'  # Customize the column header
