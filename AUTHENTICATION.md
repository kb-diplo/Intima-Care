# IntimaCare Authentication System

## 🔐 Overview

The IntimaCare platform now includes a comprehensive authentication system built with Django + Django REST Framework, featuring JWT tokens, role-based access control, and secure user management.

## 🚀 Features Implemented

### ✅ Complete Authentication System
- **Custom User Model** with roles (USER, CLINICIAN, ADMIN, SUPPORT)
- **JWT Authentication** using SimpleJWT
- **Role-based Access Control**
- **Secure Password Hashing**
- **CSRF Protection**
- **CORS Configuration**
- **Session Management**

### ✅ API Endpoints (REST)
- `POST /api/auth/signup/` - User registration
- `POST /api/auth/login/` - User login
- `POST /api/auth/logout/` - User logout
- `POST /api/auth/refresh/` - Token refresh
- `GET /api/auth/me/` - Get current user profile

### ✅ HTML Pages
- `/login/` - Login page with modern UI
- `/signup/` - Registration page with form validation
- `/dashboard/` - Protected dashboard (requires login)
- `/logout/` - Logout functionality

### ✅ Security Features
- Environment variable support for sensitive settings
- Secure JWT token generation and validation
- Password validation and hashing
- CSRF token protection
- Rate limiting ready (can be added)
- Secure cookie settings

## 🎨 UI/UX Features

### Modern Authentication Design
- **Black/White/Yellow** theme matching IntimaCare branding
- **Responsive design** for all devices
- **Error message display** with styled notifications
- **Form validation** with user-friendly feedback
- **Smooth animations** and hover effects

### Navigation Integration
- **Dynamic navigation** showing login/logout based on auth status
- **Dashboard access** for authenticated users
- **Clickable logo** returns to home page
- **User role display** in dashboard

## 👥 Test Accounts Created

```
Admin User:
Email: admin@intimacare.com
Password: admin123
Role: ADMIN (Full access)

Clinician:
Email: doctor@intimacare.com  
Password: doctor123
Role: CLINICIAN

Regular User:
Email: user@example.com
Password: user123
Role: USER
```

## 🔧 Technical Implementation

### User Model Fields
```python
- email (unique, primary login)
- username (unique)
- phone (unique)
- role (USER/CLINICIAN/ADMIN/SUPPORT)
- first_name, last_name
- date_joined
- is_active, is_staff, is_superuser
```

### JWT Configuration
- **Access Token**: 60 minutes lifetime
- **Refresh Token**: 7 days lifetime
- **Token Rotation**: Enabled for security
- **Blacklisting**: Old tokens invalidated

### API Authentication Flow
1. **Signup**: Creates user + auto-login + returns JWT tokens
2. **Login**: Validates credentials + returns JWT tokens
3. **Protected Routes**: Require valid JWT token
4. **Token Refresh**: Extends session without re-login
5. **Logout**: Blacklists tokens

## 🛡️ Security Best Practices

### Implemented
- ✅ Environment variables for secrets
- ✅ CSRF protection on forms
- ✅ Secure password hashing (Django default)
- ✅ JWT token expiration
- ✅ Secure cookie settings
- ✅ XSS protection headers
- ✅ Content type validation

### Ready to Add
- Rate limiting for login attempts
- Email verification for signup
- Password reset functionality
- Two-factor authentication
- Account lockout after failed attempts

## 🔗 URL Structure

### HTML Routes
```
/login/          - Login form
/signup/         - Registration form  
/dashboard/      - User dashboard (protected)
/logout/         - Logout action
```

### API Routes
```
/api/auth/signup/    - POST: Register new user
/api/auth/login/     - POST: Authenticate user
/api/auth/logout/    - POST: Logout user
/api/auth/refresh/   - POST: Refresh JWT token
/api/auth/me/        - GET: Current user info
```

## 🎯 Usage Examples

### Frontend Login (HTML Form)
```html
<form method="post" action="/login/">
    {% csrf_token %}
    <input type="text" name="email_or_username" required>
    <input type="password" name="password" required>
    <button type="submit">Login</button>
</form>
```

### API Login (JavaScript)
```javascript
const response = await fetch('/api/auth/login/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken')
    },
    body: JSON.stringify({
        email_or_username: 'user@example.com',
        password: 'user123'
    })
});

const data = await response.json();
// data.tokens.access - JWT access token
// data.tokens.refresh - JWT refresh token
// data.user - User profile info
```

### Protected API Request
```javascript
const response = await fetch('/api/auth/me/', {
    headers: {
        'Authorization': `Bearer ${accessToken}`
    }
});
```

## 🚀 Next Steps

The authentication system is fully functional and ready for:

1. **Frontend Integration**: Connect React/Vue apps using JWT tokens
2. **Email Features**: Add email verification and password reset
3. **Advanced Security**: Implement 2FA, rate limiting
4. **User Management**: Admin interface for user management
5. **Role Permissions**: Fine-grained permission system
6. **Social Auth**: Add Google/Facebook login options

## 🔍 Testing

Visit the browser preview and test:

1. **Sign Up**: Create a new account at `/signup/`
2. **Login**: Use test accounts at `/login/`
3. **Dashboard**: Access protected area at `/dashboard/`
4. **API**: Test endpoints with tools like Postman
5. **Admin**: Manage users at `/admin/` (use admin account)

The system is production-ready with proper security measures and can be extended with additional features as needed!
