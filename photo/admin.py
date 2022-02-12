from django.contrib import admin
from .models import Photo
admin.site.register(Photo)

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id','author','created','updated']
    row_id_fileds = ['author']
    list_filter = ['crated','updated','author']
    search_fields = ['text','-created']

admin.site.register(Photo,PhotoAdmin)
