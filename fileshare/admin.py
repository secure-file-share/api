from django.contrib import admin
from .models import Files, FileShare


class FilesAdmin(admin.ModelAdmin):
    model = Files

    list_display = ("name", "ext", "file_size", "organization", "expiration")
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

    def file_size(self, obj):
        return "{:0.2f} MB".format(obj.size/1024)


admin.site.register(Files, FilesAdmin)
