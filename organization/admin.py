from django.contrib import admin
from client.models import UserMeta
from .models import Organization


class OrganizationUserInline(admin.TabularInline):
    model = UserMeta
    extra = 0
    verbose_name = "Organization User"

    readonly_fields = ("user",)

    def has_delete_permission(self, request, obj):
        return False

    def has_add_permission(self, request, obj):
        return False


class OrganizationAdmin(admin.ModelAdmin):
    model = Organization

    list_display = ("name", "phone", "address_state", "address_zip")
    search_fields = ("name", "phone", "address_street1", "address_street2",
                     "address_city", "address_state", "address_country", "address_zip")
    list_filter = ("address_state", "address_country")

    fieldsets = (
        ("Company", {
            "fields": ("name", "phone", "secret_key")
        }),
        ("Address", {
            "fields": ("address_street1", "address_street2", "address_city",
                       "address_state", "address_country", "address_zip")
        }),
    )

    readonly_fields = ("secret_key",)

    inlines = (OrganizationUserInline,)


admin.site.register(Organization, OrganizationAdmin)
