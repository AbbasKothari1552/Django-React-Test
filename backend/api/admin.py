from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    # Add your custom fields to the fieldsets without duplicating existing ones
    fieldsets = (
        (None, {'fields': ('password',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Additional Info', {'fields': ('is_seller',)}),
    )
    
    # Specify the fields to be displayed in the list view
    list_display = ('email', 'first_name', 'last_name', 'is_seller', 'date_joined', 'last_login')
    
    # Add filters for the fields
    list_filter = ('is_seller', 'date_joined', 'last_login')
    
    # Specify the fields to be used in the search functionality
    search_fields = ('email', 'first_name', 'last_name')

    # Add ordering for the fields
    ordering = ('email',)

# Register the custom admin
admin.site.register(CustomUser, CustomUserAdmin)
