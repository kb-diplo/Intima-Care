from django.core.management.base import BaseCommand
from cms.models import SiteSettings, ServiceFeature


class Command(BaseCommand):
    help = 'Set up initial data for IntimaCare'

    def handle(self, *args, **options):
        self.stdout.write('Setting up initial data for IntimaCare...')
        
        # Create default site settings if none exist
        if not SiteSettings.objects.exists():
            site_settings = SiteSettings.objects.create(
                site_name="IntimaCare",
                primary_color="#FFC300",
                secondary_color="#000000",
                tagline="Your trusted telehealth platform for comprehensive healthcare solutions",
                about_text="IntimaCare is a revolutionary telehealth platform that combines cutting-edge AI technology with expert medical professionals to provide accessible, personalized healthcare solutions.",
                mission="To democratize healthcare access by providing innovative, secure, and personalized telehealth solutions.",
                vision="To become the leading global telehealth platform that seamlessly integrates artificial intelligence with human expertise.",
                contact_email="info@intimacare.com",
                contact_phone="+1 (555) 123-4567",
                footer_text="© IntimaCare 2025 - Empowering Health, Everywhere"
            )
            self.stdout.write(self.style.SUCCESS('Created site settings'))
        else:
            self.stdout.write('Site settings already exist')
        
        # Create default service features if none exist
        if not ServiceFeature.objects.exists():
            services = [
                {
                    'name': 'AI Consultation',
                    'description': 'Get instant health insights and preliminary assessments through our advanced AI system. Available 24/7 for immediate guidance.',
                    'order': 1
                },
                {
                    'name': 'Clinician Consultations',
                    'description': 'Connect with qualified healthcare professionals for personalized medical consultations and expert care.',
                    'order': 2
                },
                {
                    'name': 'Daily Tracking',
                    'description': 'Monitor your health metrics and symptoms with our comprehensive tracking tools and detailed reports.',
                    'order': 3
                },
                {
                    'name': 'Red-Flag Alerts',
                    'description': 'Receive immediate notifications for critical health indicators that require urgent attention.',
                    'order': 4
                },
                {
                    'name': 'Anonymous Community Support',
                    'description': 'Connect with others in a safe, anonymous environment for peer support and shared experiences.',
                    'order': 5
                }
            ]
            
            for service_data in services:
                ServiceFeature.objects.create(**service_data)
            
            self.stdout.write(self.style.SUCCESS('Created default service features'))
        else:
            self.stdout.write('Service features already exist')
        
        self.stdout.write(self.style.SUCCESS('Initial data setup complete!'))
        self.stdout.write('Next steps:')
        self.stdout.write('1. Run: python manage.py createsuperuser')
        self.stdout.write('2. Visit /admin to customize content')
        self.stdout.write('3. Upload logo and customize colors')
