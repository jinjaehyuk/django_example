from django.contrib import admin
from .models import Photo

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id','author','created','updated']
    row_id_fileds = ['author']
    list_filter = ['created','updated','author']
    search_fields = ['text','-created']
    ordering = ['-updated','-created']

admin.site.register(Photo, PhotoAdmin)
