from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ('username', 'email', 'birthdate', 'is_staff')

    fieldsets = UserAdmin.fieldsets + (
        ("Additional Information", {'fields': ('birthdate',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Information", {'fields': ('birthdate',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
