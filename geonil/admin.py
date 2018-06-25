from django.contrib import admin

from .models import Show
# Register your models here.
@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ['name','title','content','create_at','update_at']
