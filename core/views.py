from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from cms.models import SiteSettings, HomepageSection, FAQ, LegalDocument, ServiceFeature
from .forms import ContactForm


def home(request):
    """Homepage view"""
    homepage_sections = HomepageSection.objects.filter(active=True)
    context = {
        'homepage_sections': homepage_sections,
    }
    return render(request, 'core/home.html', context)


def about(request):
    """About page view"""
    return render(request, 'core/about.html')


def services(request):
    """Services page view"""
    service_features = ServiceFeature.objects.filter(active=True)
    context = {
        'service_features': service_features,
    }
    return render(request, 'core/services.html', context)


def contact(request):
    """Contact page view with form handling"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
    }
    return render(request, 'core/contact.html', context)


def faq(request):
    """FAQ page view"""
    faqs = FAQ.objects.filter(active=True)
    context = {
        'faqs': faqs,
    }
    return render(request, 'core/faq.html', context)


def legal_document(request, slug):
    """Legal document view (Privacy, Terms, etc.)"""
    document = get_object_or_404(LegalDocument, slug=slug)
    context = {
        'document': document,
    }
    return render(request, 'core/legal_document.html', context)
