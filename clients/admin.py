from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.utils.translation import gettext_lazy as _

from clients.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        'email',
    )
    list_per_page = 25
    fieldsets = (
        (
            None, {
                'fields': ('username', 'password')
            }
        ),
        (
            _('User data'), {
                'fields': ('first_name', 'last_name', 'gender', 'email', 'avatar',)
            }
        ),
        (
            _('User coordinates'), {
                'fields': ('latitude', 'longitude',)
            }
        ),
        (
            _('Important dates'), {
                'fields': ('last_login', 'date_joined')
            }
        ),
    )
    list_display_links = (
        'username',
        'first_name',
        'last_name',
    )
