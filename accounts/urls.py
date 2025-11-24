from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

# API URLs
api_urlpatterns = [
    path('signup/', views.signup_api, name='signup_api'),
    path('login/', views.login_api, name='login_api'),
    path('logout/', views.logout_api, name='logout_api'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', views.user_profile_api, name='user_profile_api'),
]

# HTML URLs
urlpatterns = [
    # Authentication routes
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    
    # Role-based dashboard routes
    path('dashboard/patient/', views.patient_dashboard_view, name='patient_dashboard'),
    path('dashboard/clinician/', views.clinician_dashboard_view, name='clinician_dashboard'),
    path('dashboard/organization/', views.organization_dashboard_view, name='organization_dashboard'),
    
    # Legacy dashboard redirect
    path('dashboard/', views.dashboard_redirect_view, name='dashboard'),
    
    # API routes
    path('api/auth/', include(api_urlpatterns)),
]
