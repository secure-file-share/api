from django.contrib import admin
from .models import Organization


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


admin.site.register(Organization, OrganizationAdmin)
