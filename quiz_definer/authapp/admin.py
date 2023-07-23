from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


# creating helper class for admin form
class MainUserAdmin(UserAdmin):
    """
    this is a helper class for user admin panel, used to define:
    -the view of the form
    -ordering
    -searching
    """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("email", "nickname", "is_staff", "is_active",)
    list_filter = ("email", "nickname", "is_staff", "is_active",)
    # defining fieldsets
    fieldsets = (
        (None, {"fields": ("email", "password", "nickname")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "nickname",
                "is_active", "groups", "user_permissions", "is_staff"
            )}
        ),
    )
    search_fields = ("nickname",)
    ordering = ("nickname",)


# register model and panel
admin.site.register(User, MainUserAdmin)
