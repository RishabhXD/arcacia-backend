from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *
from import_export.admin import ExportActionMixin

class BlogPostAdmin(ExportActionMixin,SummernoteModelAdmin): 
    exclude = ('slug',)
    list_display = ('id', 'title', 'category', 'date_created','author_name')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_per_page = 25
    summernote_fields = ('content',)

class ContactPostAdmin(ExportActionMixin,SummernoteModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'email','city')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_per_page = 25

class DealerPostAdmin(ExportActionMixin,SummernoteModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'email','profession')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_per_page = 25

admin.site.register(Blog, BlogPostAdmin)
admin.site.register(Contact,ContactPostAdmin)
admin.site.register(Dealer,DealerPostAdmin)
