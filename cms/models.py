from django.db import models
from django.core.validators import FileExtensionValidator


class SiteSettings(models.Model):
    """Global site settings and configuration"""
    site_name = models.CharField(max_length=100, default="IntimaCare")
    logo = models.ImageField(
        upload_to='logos/', 
        blank=True, 
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'svg'])]
    )
    primary_color = models.CharField(max_length=7, default="#FFC300", help_text="Hex color code")
    secondary_color = models.CharField(max_length=7, default="#000000", help_text="Hex color code")
    tagline = models.CharField(max_length=200, default="Your trusted telehealth platform")
    about_text = models.TextField(blank=True)
    mission = models.TextField(blank=True)
    vision = models.TextField(blank=True)
    contact_email = models.EmailField(default="info@intimacare.com")
    contact_phone = models.CharField(max_length=20, default="+1 (555) 123-4567")
    footer_text = models.CharField(max_length=200, default="© IntimaCare 2025")
    
    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"
    
    def __str__(self):
        return f"Site Settings - {self.site_name}"
    
    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and SiteSettings.objects.exists():
            raise ValueError('Only one SiteSettings instance is allowed')
        return super().save(*args, **kwargs)


class HomepageSection(models.Model):
    """Dynamic sections for the homepage"""
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    description = models.TextField()
    image = models.ImageField(
        upload_to='homepage_sections/', 
        blank=True, 
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'webp'])]
    )
    active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0, help_text="Order of appearance on homepage")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = "Homepage Section"
        verbose_name_plural = "Homepage Sections"
    
    def __str__(self):
        return self.title


class FAQ(models.Model):
    """Frequently Asked Questions"""
    question = models.CharField(max_length=300)
    answer = models.TextField()
    active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0, help_text="Order of appearance")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
    
    def __str__(self):
        return self.question


class LegalDocument(models.Model):
    """Legal documents like Privacy Policy, Terms, etc."""
    DOCUMENT_TYPES = [
        ('privacy', 'Privacy Policy'),
        ('terms', 'Terms & Conditions'),
        ('cookies', 'Cookies Policy'),
        ('accessibility', 'Accessibility Statement'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="URL slug for the document")
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPES, unique=True)
    content = models.TextField(help_text="Full content of the legal document")
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['title']
        verbose_name = "Legal Document"
        verbose_name_plural = "Legal Documents"
    
    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    """Contact form submissions"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-date_created']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
    
    def __str__(self):
        return f"Message from {self.name} - {self.date_created.strftime('%Y-%m-%d')}"


class ServiceFeature(models.Model):
    """Platform service features"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, blank=True, help_text="CSS class for icon")
    active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Service Feature"
        verbose_name_plural = "Service Features"
    
    def __str__(self):
        return self.name
