from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "first_name",
        "last_name",
        "avatar",
        "is_staff",
        "is_active",
        "is_superuser",
        "last_login",
    )
    list_filter = ("is_staff", "last_login")
    search_fields = ("email", "last_login")
