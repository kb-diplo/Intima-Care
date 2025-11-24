from django.core.management.base import BaseCommand
from cms.models import LegalDocument


class Command(BaseCommand):
    help = 'Create legal documents for IntimaCare'

    def handle(self, *args, **options):
        self.stdout.write('Creating legal documents...')
        
        # Privacy Policy
        privacy_policy, created = LegalDocument.objects.get_or_create(
            slug='privacy-policy',
            defaults={
                'title': 'Privacy Policy',
                'document_type': 'privacy',
                'content': '''# Privacy Policy

**Effective Date:** November 24, 2025

## Introduction

IntimaCare ("we," "our," or "us") is committed to protecting your privacy and ensuring the security of your personal health information. This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you use our telehealth platform.

## Information We Collect

### Personal Information
- Name, email address, phone number
- Date of birth and demographic information
- Health insurance information
- Payment and billing information

### Health Information
- Medical history and health records
- Symptoms and health concerns
- Consultation notes and treatment plans
- Health tracking data and metrics

### Technical Information
- Device information and IP address
- Usage data and platform interactions
- Cookies and similar technologies

## How We Use Your Information

- Provide telehealth services and consultations
- Maintain and improve our platform
- Communicate with you about your health and services
- Process payments and billing
- Comply with legal and regulatory requirements

## Information Sharing

We do not sell, trade, or rent your personal health information. We may share information only:
- With your healthcare providers (with consent)
- For legal compliance or safety reasons
- With service providers under strict confidentiality agreements

## Data Security

We implement industry-standard security measures including:
- End-to-end encryption for all communications
- Secure data storage and transmission
- Regular security audits and updates
- Access controls and authentication measures

## Your Rights

- Access and review your personal information
- Request corrections to inaccurate data
- Request deletion of your information
- Opt-out of certain communications

## Contact Us

For questions about this Privacy Policy, contact us at:
- Email: privacy@intimacare.com
- Phone: +1 (555) 123-4567'''
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Created Privacy Policy'))
        else:
            self.stdout.write('Privacy Policy already exists')

        # Terms & Conditions
        terms, created = LegalDocument.objects.get_or_create(
            slug='terms-conditions',
            defaults={
                'title': 'Terms & Conditions',
                'document_type': 'terms',
                'content': '''# Terms & Conditions

**Effective Date:** November 24, 2025

## Agreement to Terms

By accessing and using IntimaCare's telehealth platform, you agree to be bound by these Terms & Conditions and all applicable laws and regulations.

## Description of Service

IntimaCare provides telehealth services including:
- AI-powered health consultations
- Access to licensed healthcare professionals
- Health tracking and monitoring tools
- Community support features

## User Responsibilities

### Account Security
- Maintain confidentiality of your account credentials
- Notify us immediately of any unauthorized access
- Provide accurate and current information

### Appropriate Use
- Use services only for legitimate healthcare purposes
- Follow healthcare provider instructions
- Respect other users and community guidelines

## Medical Disclaimer

- Our AI system provides preliminary insights, not medical diagnoses
- Always consult with licensed healthcare professionals for medical decisions
- In emergencies, contact local emergency services immediately
- We do not guarantee specific health outcomes

## Privacy and Data Protection

Your privacy is protected under our Privacy Policy and applicable healthcare privacy laws including HIPAA.

## Payment Terms

- Fees are due as specified in your service plan
- We accept various payment methods
- Refunds are subject to our refund policy
- Insurance coverage varies by plan and provider

## Limitation of Liability

IntimaCare's liability is limited to the maximum extent permitted by law. We are not liable for:
- Medical outcomes or treatment results
- Technical issues or service interruptions
- Third-party actions or services

## Termination

We may terminate or suspend your account for:
- Violation of these terms
- Fraudulent or inappropriate behavior
- Non-payment of fees
- Legal or regulatory requirements

## Changes to Terms

We reserve the right to modify these terms at any time. Changes will be posted on our platform and communicated to users.

## Contact Information

For questions about these Terms & Conditions:
- Email: legal@intimacare.com
- Phone: +1 (555) 123-4567'''
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Created Terms & Conditions'))
        else:
            self.stdout.write('Terms & Conditions already exist')

        # Cookies Policy
        cookies, created = LegalDocument.objects.get_or_create(
            slug='cookies-policy',
            defaults={
                'title': 'Cookies Policy',
                'document_type': 'cookies',
                'content': '''# Cookies Policy

**Effective Date:** November 24, 2025

## What Are Cookies

Cookies are small text files that are placed on your device when you visit our website. They help us provide you with a better experience by remembering your preferences and improving our services.

## Types of Cookies We Use

### Essential Cookies
- Required for basic website functionality
- Enable secure login and account access
- Remember your session information
- Cannot be disabled without affecting site functionality

### Performance Cookies
- Help us understand how visitors use our site
- Collect anonymous information about page visits
- Allow us to improve site performance and user experience
- Can be disabled in your browser settings

### Functional Cookies
- Remember your preferences and settings
- Provide enhanced features and personalization
- Improve your overall user experience
- Can be managed through your account settings

### Analytics Cookies
- Help us analyze website traffic and usage patterns
- Provide insights for improving our services
- Generate reports on site performance
- Data is anonymized and aggregated

## Managing Cookies

### Browser Settings
You can control cookies through your browser settings:
- Chrome: Settings > Privacy and Security > Cookies
- Firefox: Options > Privacy & Security > Cookies
- Safari: Preferences > Privacy > Cookies
- Edge: Settings > Privacy > Cookies

### Our Cookie Preferences
You can manage your cookie preferences through our cookie consent banner or in your account settings.

## Third-Party Cookies

We may use third-party services that set their own cookies:
- Google Analytics (for website analytics)
- Payment processors (for secure transactions)
- Customer support tools (for help and assistance)

These third parties have their own privacy policies and cookie practices.

## Contact Us

If you have questions about our use of cookies:
- Email: privacy@intimacare.com
- Phone: +1 (555) 123-4567'''
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Created Cookies Policy'))
        else:
            self.stdout.write('Cookies Policy already exists')

        # Accessibility Statement
        accessibility, created = LegalDocument.objects.get_or_create(
            slug='accessibility-statement',
            defaults={
                'title': 'Accessibility Statement',
                'document_type': 'accessibility',
                'content': '''# Accessibility Statement

**Effective Date:** November 24, 2025

## Our Commitment to Accessibility

IntimaCare is committed to ensuring digital accessibility for people with disabilities. We continually improve the user experience for everyone and apply relevant accessibility standards.

## Accessibility Standards

We strive to conform to the Web Content Accessibility Guidelines (WCAG) 2.1 Level AA standards. These guidelines help make web content more accessible to people with disabilities.

## Accessibility Features

### Navigation
- Consistent navigation structure across all pages
- Skip links to main content
- Logical heading hierarchy
- Keyboard navigation support

### Visual Design
- High contrast color schemes
- Scalable text and interface elements
- Clear visual focus indicators
- Alternative text for images

### Interactive Elements
- Keyboard accessible forms and controls
- Clear error messages and instructions
- Sufficient time limits for interactions
- No content that causes seizures or physical reactions

### Content
- Plain language and clear instructions
- Consistent terminology and layout
- Descriptive link text
- Structured content with proper headings

## Assistive Technology Support

Our platform is designed to work with:
- Screen readers (JAWS, NVDA, VoiceOver)
- Voice recognition software
- Keyboard-only navigation
- Screen magnification tools

## Feedback and Support

We welcome feedback on the accessibility of IntimaCare. If you encounter accessibility barriers:

### Contact Methods
- Email: accessibility@intimacare.com
- Phone: +1 (555) 123-4567
- TTY: +1 (555) 123-4568

### Response Time
We aim to respond to accessibility feedback within 2 business days and will work with you to provide the information or service you need in an accessible format.

## Legal Compliance

This accessibility statement is in accordance with:
- Americans with Disabilities Act (ADA)
- Section 508 of the Rehabilitation Act
- Web Content Accessibility Guidelines (WCAG) 2.1

## Updates

This accessibility statement was last updated on November 24, 2025. We review and update this statement regularly as we continue to improve accessibility.'''
            }
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Created Accessibility Statement'))
        else:
            self.stdout.write('Accessibility Statement already exists')

        self.stdout.write(self.style.SUCCESS('Legal documents setup complete!'))
