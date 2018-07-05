from django.contrib import admin
from .models import Food
# Register your models here.
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['id','author','title','create_at','update_at']
    list_display_links = ['title']
