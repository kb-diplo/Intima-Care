from .models import SiteSettings


def site_settings(request):
    """Make site settings available in all templates"""
    try:
        settings = SiteSettings.objects.first()
        return {'site_settings': settings}
    except SiteSettings.DoesNotExist:
        return {'site_settings': None}
