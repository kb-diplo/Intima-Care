from django.core.management.base import BaseCommand
from accounts.models import User


class Command(BaseCommand):
    help = 'Create test users for IntimaCare authentication system'

    def handle(self, *args, **options):
        self.stdout.write('Creating test users...')
        
        # Create admin user (organization role with admin privileges)
        admin_user, created = User.objects.get_or_create(
            email='admin@intimacare.com',
            defaults={
                'username': 'admin@intimacare.com',
                'full_name': 'IntimaCare Administrator',
                'phone': '+1-555-000-0001',
                'role': 'ORGANIZATION',
                'is_staff': True,
                'is_superuser': True,
                'is_verified': True,
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
            self.stdout.write(self.style.SUCCESS('Created admin user: admin@intimacare.com / admin123'))
        else:
            self.stdout.write('Admin user already exists')

        # Create clinician user
        clinician_user, created = User.objects.get_or_create(
            email='doctor@intimacare.com',
            defaults={
                'username': 'doctor@intimacare.com',
                'full_name': 'Dr. Sarah Smith',
                'phone': '+1-555-000-0002',
                'role': 'CLINICIAN',
                'is_verified': True,
            }
        )
        if created:
            clinician_user.set_password('doctor123')
            clinician_user.save()
            self.stdout.write(self.style.SUCCESS('Created clinician user: doctor@intimacare.com / doctor123'))
        else:
            self.stdout.write('Clinician user already exists')

        # Create patient user
        patient_user, created = User.objects.get_or_create(
            email='patient@example.com',
            defaults={
                'username': 'patient@example.com',
                'full_name': 'John Doe',
                'phone': '+1-555-000-0003',
                'role': 'PATIENT',
                'is_verified': True,
            }
        )
        if created:
            patient_user.set_password('patient123')
            patient_user.save()
            self.stdout.write(self.style.SUCCESS('Created patient user: patient@example.com / patient123'))
        else:
            self.stdout.write('Patient user already exists')

        # Create organization user
        org_user, created = User.objects.get_or_create(
            email='org@healthcorp.com',
            defaults={
                'username': 'org@healthcorp.com',
                'full_name': 'HealthCorp Organization',
                'phone': '+1-555-000-0004',
                'role': 'ORGANIZATION',
                'is_verified': True,
            }
        )
        if created:
            org_user.set_password('org123')
            org_user.save()
            self.stdout.write(self.style.SUCCESS('Created organization user: org@healthcorp.com / org123'))
        else:
            self.stdout.write('Organization user already exists')

        self.stdout.write(self.style.SUCCESS('\nTest users created successfully!'))
        self.stdout.write('You can now test the authentication system with these accounts.')
        self.stdout.write('\nAPI Endpoints available:')
        self.stdout.write('- POST /api/auth/signup/')
        self.stdout.write('- POST /api/auth/login/')
        self.stdout.write('- POST /api/auth/logout/')
        self.stdout.write('- POST /api/auth/refresh/')
        self.stdout.write('- GET /api/auth/me/')
        self.stdout.write('\nHTML Pages available:')
        self.stdout.write('- /login/')
        self.stdout.write('- /signup/')
        self.stdout.write('- /dashboard/')
        self.stdout.write('- /logout/')
