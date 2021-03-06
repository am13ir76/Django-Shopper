from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as UserAdminBase
from django.utils.translation import gettext as _

from core import models


class UserAdmin(UserAdminBase):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Personal Information'),
            {
                'fields': ('name',)
            }
        ),
        (
            _('Permissions'),
            {
                'fields': ('is_active', 'is_staff', 'is_superuser')
            }
        ),
        (
            _('Important dates'),
            {
                'fields': ('last_login',)
            }
        )
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Product)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)
