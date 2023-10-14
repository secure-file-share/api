from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User, UserMeta
from .forms import UserChangeForm, UserCreationForm, GroupAdminForm


class UserMetaAdmin(admin.StackedInline):
    model = UserMeta
    extra = 0


class MyUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'first_name', 'last_name', 'email',
                    'is_superuser', 'is_active')
    list_filter = [
        'is_superuser',
        'is_staff',
        'is_active',
    ]
    fieldsets = (
        ("User Info", {'fields': ('first_name', 'last_name',
                                  'username', 'email', 'password')}),
        ('Permissions', {
         'fields': ('is_superuser', 'is_staff', 'is_active')}),
        ("Misc.", {"fields": ("date_joined", "last_login")})
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
         ),
    )
    search_fields = ('email', 'username', "first_name",
                     "last_name")
    readonly_fields = ("date_joined", "last_login")
    ordering = ('email',)
    filter_horizontal = ()
    inlines = (UserMetaAdmin,)


class GroupAdmin(admin.ModelAdmin):
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']


admin.site.unregister(Group)
admin.site.register(User, MyUserAdmin)
admin.site.register(Group, GroupAdmin)
