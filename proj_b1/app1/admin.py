from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *

# Register your models here.
@admin.register(Talaba)
class StudentAdmin(ModelAdmin):
    list_display = ('ism', 'universitet', 'kurs', 'shahar')
    list_editable = ('universitet', 'kurs')
    list_filter = ('yosh', 'universitet')
    search_fields = ('ism', 'yosh',)


admin.site.register(Author)
admin.site.register(Book)


@admin.register(Record)
class RecordAdmin(ModelAdmin):
    list_display = ('student', 'book', 'qaytardi')
    list_display_links = ('book',)
    list_editable = ('student',)
    search_fields = ('student__ism',)
    autocomplete_fields = ('student',)





