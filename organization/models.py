from django.db import models
from alpha.utilities import random_string
from alpha.extra_models import TimestampWithRecord


class Organization(TimestampWithRecord):
    """
    Organization Data Model

    ---
    Fields

    name : Char
    phone : Char
    address_street1 : Char
    address_street2 : Char
    address_city : Char
    address_state : Char
    address_country : Char
    address_zip : Char
    secret_code : Char
    """

    # BASIC INFO
    name = models.CharField(max_length=150, verbose_name="Name",
                            help_text="Full legal name of the organization")
    phone = models.CharField(max_length=20, verbose_name="Contact Phone",
                             help_text="Primary contact phone number of the organization")

    # ADDRESS
    address_street1 = models.CharField(
        max_length=150, verbose_name="Address Street 1", help_text="Street Address of the organization")
    address_street2 = models.CharField(max_length=150, verbose_name="Address Street 2",
                                       help_text="Street Address of the organization", blank=True, null=True)
    address_city = models.CharField(
        max_length=150, verbose_name="Address City", help_text="City Address of the organization", blank=True, null=True)
    address_state = models.CharField(
        max_length=150, verbose_name="Address State", help_text="State Address of the organization", blank=True, null=True)
    address_country = models.CharField(
        max_length=150, verbose_name="Address Country", help_text="Country Address of the organization", blank=True, null=True)
    address_zip = models.CharField(
        max_length=150, verbose_name="Address ZIP Code", help_text="Zip Code of the organization", blank=True, null=True)

    # SYSTEM INFO
    secret_key = models.CharField(
        max_length=50, editable=False, default=random_string)

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organization"

    def __str__(self):
        return self.name

    @property
    def full_address(self):
        return f"{self.address_street1}, {self.address_street2}, {self.address_city}, {self.address_state}, {self.address_zip}, {self.address_country}"

    @property
    def address(self):
        if self.address_city and self.address_state:
            return f"{self.address_street1}, {self.address_city},{self.address_state}"
        else:
            return f"{self.address_street1}"
