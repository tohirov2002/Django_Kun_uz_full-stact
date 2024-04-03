from django.contrib import admin

# Register your models here.
from .models import Category,News

admin.site.register(Category)
admin.site.register(News)