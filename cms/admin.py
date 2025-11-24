from django.contrib import admin
from django.utils.html import format_html
from django.db.models import Count
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import SiteSettings, HomepageSection, FAQ, LegalDocument, ContactMessage, ServiceFeature


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    """Enhanced Site Settings Admin"""
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('site_name', 'logo', 'tagline'),
            'description': 'Core site information and branding'
        }),
        ('Colors & Branding', {
            'fields': ('primary_color', 'secondary_color'),
            'description': 'Color scheme for the website'
        }),
        ('About Content', {
            'fields': ('about_text', 'mission', 'vision'),
            'description': 'Content for the About page'
        }),
        ('Contact Information', {
            'fields': ('contact_email', 'contact_phone'),
            'description': 'Contact details displayed on the site'
        }),
        ('Footer', {
            'fields': ('footer_text',),
            'description': 'Footer content'
        }),
    )
    
    def has_add_permission(self, request):
        # Only allow one instance
        return not SiteSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Don't allow deletion of site settings
        return False
    
    def changelist_view(self, request, extra_context=None):
        """Add custom context to changelist"""
        extra_context = extra_context or {}
        extra_context['title'] = 'Site Configuration'
        return super().changelist_view(request, extra_context)


@admin.register(HomepageSection)
class HomepageSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'active', 'order', 'created_at')
    list_filter = ('active', 'created_at')
    search_fields = ('title', 'subtitle', 'description')
    list_editable = ('active', 'order')
    ordering = ('order', 'created_at')
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'subtitle', 'description', 'image')
        }),
        ('Settings', {
            'fields': ('active', 'order')
        }),
    )


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'active', 'order', 'created_at')
    list_filter = ('active', 'created_at')
    search_fields = ('question', 'answer')
    list_editable = ('active', 'order')
    ordering = ('order', 'created_at')
    
    fieldsets = (
        ('FAQ Content', {
            'fields': ('question', 'answer')
        }),
        ('Settings', {
            'fields': ('active', 'order')
        }),
    )


@admin.register(LegalDocument)
class LegalDocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'document_type', 'last_updated')
    list_filter = ('document_type', 'last_updated')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        ('Document Information', {
            'fields': ('title', 'slug', 'document_type')
        }),
        ('Content', {
            'fields': ('content',)
        }),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """Enhanced Contact Message Admin with better management"""
    
    list_display = ('name', 'email', 'subject', 'read_status', 'is_read', 'date_created', 'days_ago')
    list_filter = ('is_read', 'date_created')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message', 'date_created')
    list_editable = ('is_read',)
    ordering = ('-date_created',)
    date_hierarchy = 'date_created'
    
    def has_add_permission(self, request):
        # Contact messages are only created through the form
        return False
    
    def read_status(self, obj):
        """Display read status with color coding"""
        if obj.is_read:
            return format_html(
                '<span style="color: green; font-weight: bold;">✓ Read</span>'
            )
        else:
            return format_html(
                '<span style="color: red; font-weight: bold;">✗ Unread</span>'
            )
    read_status.short_description = 'Status'
    
    def days_ago(self, obj):
        """Show how many days ago the message was sent"""
        from django.utils import timezone
        days = (timezone.now() - obj.date_created).days
        if days == 0:
            return "Today"
        elif days == 1:
            return "Yesterday"
        else:
            return f"{days} days ago"
    days_ago.short_description = 'Received'
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'date_created')
        }),
        ('Message', {
            'fields': ('subject', 'message'),
            'classes': ('wide',)
        }),
        ('Status', {
            'fields': ('is_read',)
        }),
    )
    
    actions = ['mark_as_read', 'mark_as_unread']
    
    def mark_as_read(self, request, queryset):
        """Bulk mark messages as read"""
        updated = queryset.update(is_read=True)
        self.message_user(request, f'{updated} messages marked as read.')
    mark_as_read.short_description = "Mark selected messages as read"
    
    def mark_as_unread(self, request, queryset):
        """Bulk mark messages as unread"""
        updated = queryset.update(is_read=False)
        self.message_user(request, f'{updated} messages marked as unread.')
    mark_as_unread.short_description = "Mark selected messages as unread"


@admin.register(ServiceFeature)
class ServiceFeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'order', 'created_at')
    list_filter = ('active', 'created_at')
    search_fields = ('name', 'description')
    list_editable = ('active', 'order')
    ordering = ('order', 'name')
    
    fieldsets = (
        ('Feature Information', {
            'fields': ('name', 'description', 'icon_class')
        }),
        ('Settings', {
            'fields': ('active', 'order')
        }),
    )


# Custom Admin Dashboard
class IntimaCareAdminSite(admin.AdminSite):
    """Custom admin site with enhanced dashboard"""
    
    site_header = "IntimaCare Administration"
    site_title = "IntimaCare Admin"
    index_title = "IntimaCare Management Dashboard"
    
    def index(self, request, extra_context=None):
        """Enhanced admin dashboard with analytics"""
        from accounts.models import User
        from django.utils import timezone
        from datetime import timedelta
        
        extra_context = extra_context or {}
        
        # User statistics
        total_users = User.objects.count()
        patients = User.objects.filter(role='PATIENT').count()
        clinicians = User.objects.filter(role='CLINICIAN').count()
        organizations = User.objects.filter(role='ORGANIZATION').count()
        
        # Recent activity (last 30 days)
        thirty_days_ago = timezone.now() - timedelta(days=30)
        recent_users = User.objects.filter(date_joined__gte=thirty_days_ago).count()
        
        # Contact messages
        unread_messages = ContactMessage.objects.filter(is_read=False).count()
        total_messages = ContactMessage.objects.count()
        
        # Content statistics
        active_homepage_sections = HomepageSection.objects.filter(active=True).count()
        active_faqs = FAQ.objects.filter(active=True).count()
        active_services = ServiceFeature.objects.filter(active=True).count()
        
        extra_context.update({
            'dashboard_stats': {
                'total_users': total_users,
                'patients': patients,
                'clinicians': clinicians,
                'organizations': organizations,
                'recent_users': recent_users,
                'unread_messages': unread_messages,
                'total_messages': total_messages,
                'active_homepage_sections': active_homepage_sections,
                'active_faqs': active_faqs,
                'active_services': active_services,
            }
        })
        
        return super().index(request, extra_context)

# Replace default admin site
admin_site = IntimaCareAdminSite(name='intimacare_admin')

# Re-register all models with the custom admin site
from accounts.models import User
from accounts.admin import CustomUserAdmin

admin_site.register(User, CustomUserAdmin)
admin_site.register(SiteSettings, SiteSettingsAdmin)
admin_site.register(HomepageSection, HomepageSectionAdmin)
admin_site.register(FAQ, FAQAdmin)
admin_site.register(LegalDocument, LegalDocumentAdmin)
admin_site.register(ContactMessage, ContactMessageAdmin)
admin_site.register(ServiceFeature, ServiceFeatureAdmin)

# Keep the default registrations for compatibility
admin.site.site_header = "IntimaCare Admin"
admin.site.site_title = "IntimaCare Admin Portal"
admin.site.index_title = "Welcome to IntimaCare Administration"
