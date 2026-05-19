from django.contrib import admin

from .models import Experience, Project, Skill


admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Portfolio Content Dashboard"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "tech_stack", "featured", "order", "created_at")
    list_filter = ("featured", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "summary", "description", "tech_stack")
    list_editable = ("featured", "order")
    ordering = ("order", "-created_at")

    class Media:
        css = {"all": ("css/admin.css",)}


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "proficiency", "is_featured", "order")
    list_filter = ("category", "is_featured")
    search_fields = ("name",)
    list_editable = ("proficiency", "is_featured", "order")
    ordering = ("category", "order", "name")

    class Media:
        css = {"all": ("css/admin.css",)}


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("title", "organization", "type", "period", "is_current", "order")
    list_filter = ("type", "is_current")
    search_fields = ("title", "organization", "description")
    list_editable = ("is_current", "order")
    ordering = ("order",)

    class Media:
        css = {"all": ("css/admin.css",)}
