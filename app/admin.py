from django.contrib import admin
from .models import Imges
# Register your models here.

@admin.register(Imges)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','photo','date']