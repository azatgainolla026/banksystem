from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAccount


class CustomUserAdmin(UserAdmin):
    model = UserAccount
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'balance')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('balance',)}),
    )


admin.site.register(UserAccount, CustomUserAdmin)
