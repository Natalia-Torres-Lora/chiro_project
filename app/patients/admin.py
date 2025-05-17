from django.contrib import admin
from .models import Patient

# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'date_of_birth')
    search_fields = ('user__first_name', 'user__last_name', 'phone_number')