from django.core.management.base import BaseCommand
from cms.models import SiteSettings, HomepageSection, FAQ, ServiceFeature
from accounts.models import User


class Command(BaseCommand):
    help = 'Fix admin content display issues and populate proper data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Fixing admin content and display issues...'))
        
        # Fix SiteSettings
        site_settings, created = SiteSettings.objects.get_or_create(
            defaults={
                'site_name': 'IntimaCare',
                'tagline': 'Your Trusted Telehealth Platform',
                'primary_color': '#FFC300',
                'secondary_color': '#000000',
                'about_text': 'IntimaCare is a comprehensive telehealth platform connecting patients with healthcare professionals through secure, AI-powered consultations.',
                'mission': 'To make quality healthcare accessible to everyone, everywhere, through innovative technology and compassionate care.',
                'vision': 'A world where distance is no barrier to receiving excellent healthcare.',
                'contact_email': 'info@intimacare.com',
                'contact_phone': '+1 (555) 123-4567',
                'footer_text': '© 2025 IntimaCare. All rights reserved.'
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('+ Created site settings'))
        else:
            # Update existing settings to fix any display issues
            site_settings.site_name = 'IntimaCare'
            site_settings.tagline = 'Your Trusted Telehealth Platform'
            if not site_settings.about_text or len(site_settings.about_text.strip()) == 0:
                site_settings.about_text = 'IntimaCare is a comprehensive telehealth platform connecting patients with healthcare professionals through secure, AI-powered consultations.'
            if not site_settings.mission or len(site_settings.mission.strip()) == 0:
                site_settings.mission = 'To make quality healthcare accessible to everyone, everywhere, through innovative technology and compassionate care.'
            if not site_settings.vision or len(site_settings.vision.strip()) == 0:
                site_settings.vision = 'A world where distance is no barrier to receiving excellent healthcare.'
            site_settings.save()
            self.stdout.write(self.style.SUCCESS('+ Updated site settings'))
        
        # Fix Homepage Sections
        homepage_sections = [
            {
                'title': 'AI-Powered Health Consultations',
                'subtitle': 'Get instant health insights',
                'description': 'Our advanced AI system provides preliminary health assessments and connects you with the right healthcare professionals for your needs.',
                'order': 1
            },
            {
                'title': 'Secure Telemedicine Platform',
                'subtitle': 'Healthcare from anywhere',
                'description': 'Connect with licensed healthcare providers through our secure, HIPAA-compliant video consultation platform.',
                'order': 2
            },
            {
                'title': 'Comprehensive Health Tracking',
                'subtitle': 'Monitor your wellness journey',
                'description': 'Track symptoms, medications, and health metrics with our intuitive dashboard designed for patients and healthcare providers.',
                'order': 3
            }
        ]
        
        for section_data in homepage_sections:
            section, created = HomepageSection.objects.get_or_create(
                title=section_data['title'],
                defaults=section_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'+ Created homepage section: {section.title}'))
        
        # Fix FAQs
        faqs = [
            {
                'question': 'How do I schedule a consultation?',
                'answer': 'Simply log into your dashboard, select "Book Consultation" and choose from available healthcare providers. You can schedule appointments based on your preferred time and the doctor\'s availability.',
                'order': 1
            },
            {
                'question': 'Is my health information secure?',
                'answer': 'Yes, IntimaCare is fully HIPAA-compliant. All your health information is encrypted and stored securely. We never share your personal health data without your explicit consent.',
                'order': 2
            },
            {
                'question': 'What types of healthcare services are available?',
                'answer': 'We offer general consultations, specialist referrals, prescription management, health monitoring, and AI-powered health assessments. More specialized services are being added regularly.',
                'order': 3
            },
            {
                'question': 'How does the AI health assessment work?',
                'answer': 'Our AI system analyzes your symptoms, medical history, and health data to provide preliminary insights and recommendations. It helps determine if you need immediate care or can wait for a scheduled consultation.',
                'order': 4
            }
        ]
        
        for faq_data in faqs:
            faq, created = FAQ.objects.get_or_create(
                question=faq_data['question'],
                defaults=faq_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'+ Created FAQ: {faq.question[:50]}...'))
        
        # Fix Service Features
        services = [
            {
                'name': 'AI Health Consultations',
                'description': 'Get instant health insights powered by advanced artificial intelligence',
                'icon_class': 'fas fa-brain',
                'order': 1
            },
            {
                'name': 'Video Consultations',
                'description': 'Secure, high-quality video calls with licensed healthcare providers',
                'icon_class': 'fas fa-video',
                'order': 2
            },
            {
                'name': 'Health Tracking',
                'description': 'Monitor symptoms, medications, and vital signs in one place',
                'icon_class': 'fas fa-heartbeat',
                'order': 3
            },
            {
                'name': 'Prescription Management',
                'description': 'Digital prescriptions and medication reminders',
                'icon_class': 'fas fa-pills',
                'order': 4
            },
            {
                'name': 'Secure Messaging',
                'description': 'HIPAA-compliant messaging with your healthcare team',
                'icon_class': 'fas fa-comments',
                'order': 5
            },
            {
                'name': '24/7 Support',
                'description': 'Round-the-clock technical and medical support',
                'icon_class': 'fas fa-clock',
                'order': 6
            }
        ]
        
        for service_data in services:
            service, created = ServiceFeature.objects.get_or_create(
                name=service_data['name'],
                defaults=service_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'+ Created service: {service.name}'))
        
        # Fix user display names
        users_updated = 0
        for user in User.objects.all():
            if not user.full_name or len(user.full_name.strip()) == 0:
                if user.first_name and user.last_name:
                    user.full_name = f"{user.first_name} {user.last_name}"
                elif user.username:
                    user.full_name = user.username.replace('_', ' ').title()
                else:
                    user.full_name = user.email.split('@')[0].replace('.', ' ').title()
                user.save()
                users_updated += 1
        
        if users_updated > 0:
            self.stdout.write(self.style.SUCCESS(f'+ Fixed {users_updated} user display names'))
        
        self.stdout.write(self.style.SUCCESS('\nAdmin content fix completed!'))
        self.stdout.write(self.style.SUCCESS('Now you can:'))
        self.stdout.write(self.style.SUCCESS('1. Visit /admin/cms/sitesettings/ to manage site content'))
        self.stdout.write(self.style.SUCCESS('2. Upload your logo and customize colors'))
        self.stdout.write(self.style.SUCCESS('3. Edit homepage sections, FAQs, and services'))
        self.stdout.write(self.style.SUCCESS('4. All content is now properly displayed!'))
