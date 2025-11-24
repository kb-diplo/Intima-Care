from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from django.db.models import Count
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Enhanced admin for User model with role-based management"""
    
    list_display = ('email', 'full_name', 'role_badge', 'phone', 'is_verified', 'is_active', 'date_joined')
    list_filter = ('role', 'is_active', 'is_verified', 'is_staff', 'date_joined')
    search_fields = ('email', 'username', 'full_name', 'phone')
    ordering = ('-date_joined',)
    list_editable = ('is_active', 'is_verified')
    
    # Custom fieldsets for our User model
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal Info', {
            'fields': ('full_name', 'email', 'phone')
        }),
        ('IntimaCare Settings', {
            'fields': ('role', 'is_verified'),
            'classes': ('wide',)
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
            'classes': ('collapse',)
        }),
        ('Important Dates', {
            'fields': ('last_login', 'date_joined'),
            'classes': ('collapse',)
        }),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
        ('Optional Info', {
            'classes': ('wide',),
            'fields': ('full_name', 'phone', 'role', 'is_verified', 'is_active'),
        }),
    )
    
    def role_badge(self, obj):
        """Display role as a colored badge"""
        colors = {
            'PATIENT': '#28a745',
            'CLINICIAN': '#007bff', 
            'ORGANIZATION': '#ffc107',
        }
        color = colors.get(obj.role, '#6c757d')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 8px; border-radius: 3px; font-size: 11px; font-weight: bold;">{}</span>',
            color,
            obj.get_role_display()
        )
    role_badge.short_description = 'Role'
    
    def get_queryset(self, request):
        """Optimize queries"""
        return super().get_queryset(request).select_related()
    
    actions = ['make_verified', 'make_unverified', 'activate_users', 'deactivate_users']
    
    def make_verified(self, request, queryset):
        """Bulk verify users"""
        updated = queryset.update(is_verified=True)
        self.message_user(request, f'{updated} users were successfully verified.')
    make_verified.short_description = "Mark selected users as verified"
    
    def make_unverified(self, request, queryset):
        """Bulk unverify users"""
        updated = queryset.update(is_verified=False)
        self.message_user(request, f'{updated} users were marked as unverified.')
    make_unverified.short_description = "Mark selected users as unverified"
    
    def activate_users(self, request, queryset):
        """Bulk activate users"""
        updated = queryset.update(is_active=True)
        self.message_user(request, f'{updated} users were successfully activated.')
    activate_users.short_description = "Activate selected users"
    
    def deactivate_users(self, request, queryset):
        """Bulk deactivate users"""
        updated = queryset.update(is_active=False)
        self.message_user(request, f'{updated} users were deactivated.')
    deactivate_users.short_description = "Deactivate selected users"
