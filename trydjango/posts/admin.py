from django.contrib import admin
from .models import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','updated','timestamp']
    list_display_links = ['updated']
    list_editable = ['title']
    list_filter = ['updated']
    search_fields = ['title','content']

    class Meta:
        model = Post

admin.site.register(Post,PostAdmin)