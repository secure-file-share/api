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


class FileShareAdmin(admin.ModelAdmin):
    model = FileShare

    list_display = ("unique_code", "file_name", "organization")
    search_fields = ("unique_code", "file_instance__name",
                     "file_instance__organization__name",)

    readonly_fields = ("unique_code",)

    def file_name(self, obj):
        return f"{obj.file_instance.name}.{obj.file_instance.ext}"

    def organization(self, obj):
        return obj.file_instance.organization.name


admin.site.register(Files, FilesAdmin)
admin.site.register(FileShare, FileShareAdmin)
