from django.contrib import admin
from person.models import *
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ('idnum', 'gender', 'city','postdate','volume')
    list_filter = ('postdate',)
    date_hierarchy = 'postdate'
    ordering = ('-postdate',)
    fields = ('idnum', 'gender', 'city','postdate','volume','dec','image_urls')
    search_fields = ('city','dec')
   
    # raw_id_fields = ('publisher',)

admin.site.register(Person, PersonAdmin)
