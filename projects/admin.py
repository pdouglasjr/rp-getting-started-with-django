from django.contrib import admin

from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Project)