from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'time_update', 'img', 'slug')
    list_display_link = ('id', 'title')
    search_fields = ('title', 'concent')

admin.site.register(Post, PostAdmin)