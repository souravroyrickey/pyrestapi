from django.contrib import admin
from .models import Result

# Register your models here.

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['rollnumber','name','grade','resultStatus']
    list_filter = ['resultStatus','grade']

