from django.contrib import admin
from .models import Review
# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['manager','shopid','shopname','shopurl','hosting','server','checklogin','checkcont','opinion','fitness','dateregi']
    list_display_links = ['shopname']
