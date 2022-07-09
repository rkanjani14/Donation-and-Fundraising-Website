from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id','name','phone','email','address','amount','date_added']