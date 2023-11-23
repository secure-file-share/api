from django.http import FileResponse
from django.contrib import admin, messages
from django_object_actions import DjangoObjectActions
from alpha.utilities import parse_date
from .models import Files, FileShare
from .crypto import decrypt_file


# class FileShareInline(admin.StackedInline):
#     model = FileShare
#     extra = 0
#     readonly_fields = ("unique_code",)

#     def has_change_permission(self, request, obj) -> bool:
#         return False

#     def has_add_permission(self, request, obj) -> bool:
#         return False

#     def has_delete_permission(self, request, obj) -> bool:
#         return False


class FilesAdmin(DjangoObjectActions, admin.ModelAdmin):
    model = Files

    list_display = ("name", "ext", "file_size", "organization", "expiration")
    search_fields = ("name", "organization", "uploaded_by__username")
    list_filter = ("ext", "expiration")

    fieldsets = (
        ("File", {
            "fields": ("file_instance", "expiration", "organization")
        }),
        # ("Details", {
        #     "fields": ("name", "ext", "size")
        # })
    )

    readonly_fields = ("ext", "size")

    change_actions = ("download_file_btn",)

    # inlines = (FileShareInline,)

    def download_file_btn(self, request, obj):
        # GET KEY TO DECRYPT FILE
        key = obj.organization.secret_key

        # DECRYPT FILE
        decrypted_file = decrypt_file(key, obj.file)

        return FileResponse(open(decrypted_file, "rb"))

    download_file_btn.label = "Download Decrypted File"
    download_file_btn.attrs = {
        "class": "btn btn-block btn-primary mb-3"}

    def file_size(self, obj):
        return "{:0.2f} MB".format(obj.size/1024)


class FileShareAdmin(DjangoObjectActions, admin.ModelAdmin):
    model = FileShare

    list_display = ("unique_code", "file_name",
                    "organization", "created_by", "shared_to")
    search_fields = ("unique_code", "file_instance__name",
                     "file_instance__organization__name",)

    fieldsets = (
        ("File Share", {
            "fields": ("file_instance", "shared_to", "shared_by", "unique_code", "organization", "name", "size",  "expiration"),
        }),
    )

    readonly_fields = ("unique_code", "name", "size",
                       "shared_by", "expiration", "organization")

    change_actions = ("download_file_btn",)

    def download_file_btn(self, request, obj):
        if not obj.pk:
            messages.warning(request, "No file found.")
            return

        try:
            # GET KEY TO DECRYPT FILE
            key = obj.organization.secret_key

            # DECRYPT FILE
            decrypted_file = decrypt_file(key, obj.file)

        except Exception as e:
            messages.error(request, str(e))
        else:
            return FileResponse(open(decrypted_file, "rb"), as_attachment=True)

    download_file_btn.label = "Download File"
    download_file_btn.attrs = {
        "class": "btn btn-block btn-primary mb-3"}

    def file_name(self, obj):
        return f"{obj.file_instance.name}.{obj.file_instance.ext}"

    def organization(self, obj):
        return obj.file_instance.organization.name

    def name(self, obj):
        return f"{obj.file_instance.name}.{obj.file_instance.ext}"

    def size(self, obj):
        return "{:0.2f} MB".format(obj.file_instance.size/1024)

    def shared_by(self, obj):
        return obj.file_instance.uploaded_by

    def shared_to(self, obj):
        return obj.file_instance.shared_to

    def expiration(self, obj):
        return parse_date(obj.file_instance.expiration, format="%b. %m %Y, %I:%M:%S %p")


admin.site.register(Files, FilesAdmin)
admin.site.register(FileShare, FileShareAdmin)
