from django.contrib import admin
from .models import Book

admin.site.site_header = 'LIBRARY MANAGEMENT SYSTEM'
admin.site.index_title = 'LIBRARY APP'
admin.site.site_title = 'library system'

# Register your models here.
admin.site.register(Book)