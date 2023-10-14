from django.contrib import admin
from .models import Files, FileShare


class FilesAdmin(admin.ModelAdmin):
    model = Files

    list_display = ("name", "ext", "size", "organization")
    search_fields = ("name", "organization", "uploaded_by__username")
    list_filter = ("ext", "expiration")

    fieldsets = (
        ("File", {
            "fields": ("file_instance", "expiration", "organization")
        }),
        ("Details", {
            "fields": ("name", "ext", "size")
        })
    )

    readonly_fields = ("ext", "size")


admin.site.register(Files, FilesAdmin)
