from django.contrib import admin
from .models import Project
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title","category","featured","published","updated_at")
    list_filter = ("category","featured","published")
    search_fields = ("title","short_description","description","technologies")
    list_editable = ("featured","published")
    prepopulated_fields = {"slug":("title",)}
    readonly_fields = ("created_at","updated_at")
admin.site.site_header = "Omar Gamal Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Manage portfolio content"
