from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Viewers)
class ViewersAdmin(admin.ModelAdmin):
    list_display=['fullname','email','dob','mobile','gender']
