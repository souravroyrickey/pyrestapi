from django.contrib import admin
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email','phone_number','date_joined']
    list_filter = ['date_joined']
    search_fields = ['username','email','phone_number']

