from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('privacy-policy/', views.legal_document, {'slug': 'privacy-policy'}, name='privacy_policy'),
    path('terms/', views.legal_document, {'slug': 'terms-conditions'}, name='terms'),
    path('cookies-policy/', views.legal_document, {'slug': 'cookies-policy'}, name='cookies_policy'),
    path('accessibility/', views.legal_document, {'slug': 'accessibility-statement'}, name='accessibility'),
]
