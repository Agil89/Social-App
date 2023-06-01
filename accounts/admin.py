from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': (
            'first_name', 'last_name',
             'last_login', 'last_request')}),
        ('Permissions', {'fields': ('is_active', 'is_superuser',
                                       'groups', 'user_permissions')}),
        # (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('email', 'get_full_name')
    list_filter = ('is_superuser', 'is_active', 'groups')
    search_fields = ('first_name', 'last_name', 'email')
    filter_horizontal = ('groups', 'user_permissions',)
