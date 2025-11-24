from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import User
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserSerializer
from .forms import SignupForm, LoginForm
import json


# API Views
@api_view(['POST'])
@permission_classes([AllowAny])
def signup_api(request):
    """API endpoint for role-based user registration"""
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        
        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token
        
        return Response({
            'message': 'User created successfully',
            'user': UserSerializer(user).data,
            'tokens': {
                'access': str(access_token),
                'refresh': str(refresh),
            }
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_api(request):
    """API endpoint for user login with role-based redirect"""
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        
        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        access_token = refresh.access_token
        
        return Response({
            'message': 'Login successful',
            'user': UserSerializer(user).data,
            'tokens': {
                'access': str(access_token),
                'refresh': str(refresh),
            }
        }, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_api(request):
    """API endpoint for user logout"""
    try:
        refresh_token = request.data.get('refresh_token')
        if refresh_token:
            token = RefreshToken(refresh_token)
            token.blacklist()
        
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile_api(request):
    """API endpoint to get current user profile"""
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


# HTML Views
def login_view(request):
    """HTML login page with role-based redirect"""
    if request.user.is_authenticated:
        return redirect(request.user.get_dashboard_url())
    
    if request.method == 'POST':
        form = LoginForm(request.POST, request=request)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.full_name}!')
            return redirect(user.get_dashboard_url())
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = LoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})


def signup_view(request):
    """HTML signup page with role selection"""
    if request.user.is_authenticated:
        return redirect(request.user.get_dashboard_url())
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome to IntimaCare, {user.full_name}!')
            return redirect(user.get_dashboard_url())
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)
    else:
        form = SignupForm()
    
    return render(request, 'accounts/signup.html', {'form': form})


def logout_view(request):
    """HTML logout"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')


# Role-based Dashboard Views
@login_required
def patient_dashboard_view(request):
    """Patient dashboard - only accessible by patients"""
    if request.user.role != 'PATIENT':
        return redirect(request.user.get_dashboard_url())
    
    return render(request, 'dashboard/patient.html', {
        'user': request.user
    })


@login_required
def clinician_dashboard_view(request):
    """Clinician dashboard - only accessible by clinicians"""
    if request.user.role != 'CLINICIAN':
        return redirect(request.user.get_dashboard_url())
    
    return render(request, 'dashboard/clinician.html', {
        'user': request.user
    })


@login_required
def organization_dashboard_view(request):
    """Organization dashboard - only accessible by organizations"""
    if request.user.role != 'ORGANIZATION':
        return redirect(request.user.get_dashboard_url())
    
    return render(request, 'dashboard/organization.html', {
        'user': request.user
    })


# Legacy dashboard redirect
@login_required
def dashboard_redirect_view(request):
    """Redirect to appropriate dashboard based on user role"""
    return redirect(request.user.get_dashboard_url())
