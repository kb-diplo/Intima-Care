from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom User model with role-based access for IntimaCare"""
    
    ROLE_CHOICES = [
        ('PATIENT', 'Patient'),
        ('CLINICIAN', 'Clinician'),
        ('ORGANIZATION', 'Organization'),
    ]
    
    # Core fields
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    role = models.CharField(max_length=12, choices=ROLE_CHOICES, default='PATIENT')
    is_verified = models.BooleanField(default=False)
    
    # Override username requirement - use email as primary identifier
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return f"{self.full_name} ({self.email}) - {self.get_role_display()}"
    
    def get_dashboard_url(self):
        """Return the correct dashboard URL based on user role"""
        role_urls = {
            'PATIENT': '/dashboard/patient/',
            'CLINICIAN': '/dashboard/clinician/',
            'ORGANIZATION': '/dashboard/organization/',
        }
        return role_urls.get(self.role, '/dashboard/patient/')
