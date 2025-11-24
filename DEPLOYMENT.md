# IntimaCare Deployment Guide

## PythonAnywhere Deployment

### 1. Upload Code
```bash
git clone https://github.com/kb-diplo/Intima-Care.git
cd Intima-Care
```

### 2. Install Dependencies
```bash
pip3.10 install --user -r requirements.txt
```

### 3. Environment Setup
Create a `.env` file in the project root:
```
SECRET_KEY=your-secret-key-here-generate-a-new-one
DEBUG=False
ALLOWED_HOSTS=yourusername.pythonanywhere.com
DB_PASSWORD=your-database-password
```

### 4. Database Setup
```bash
python manage.py migrate
python manage.py setup_initial_data
python manage.py create_legal_docs
python manage.py create_test_users
python manage.py collectstatic --noinput
```

### 5. Web App Configuration
In PythonAnywhere Web tab:
- **Source code:** `/home/yourusername/Intima-Care`
- **Working directory:** `/home/yourusername/Intima-Care`
- **WSGI configuration file:** Edit to point to `intimacare.wsgi`

### 6. WSGI Configuration
Edit your WSGI file:
```python
import os
import sys

# Add your project directory to sys.path
project_home = '/home/yourusername/Intima-Care'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'intimacare.production_settings'

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 7. Static Files
Configure static files mapping in PythonAnywhere:
- **URL:** `/static/`
- **Directory:** `/home/yourusername/Intima-Care/staticfiles/`

### 8. Media Files (Optional)
Configure media files mapping:
- **URL:** `/media/`
- **Directory:** `/home/yourusername/Intima-Care/media/`

## Test Accounts

After deployment, you can use these test accounts:

```
Admin: admin@intimacare.com / admin123
Patient: patient@example.com / patient123
Clinician: doctor@intimacare.com / doctor123
Organization: org@healthcorp.com / org123
```

## Features

### ✅ Implemented
- Role-based authentication (Patient/Clinician/Organization)
- SB Admin-style dashboards
- Enhanced admin interface with analytics
- Contact form and message management
- Legal document management
- Responsive design
- Professional branding

### 🔄 Coming Soon
- AI health consultations
- Patient management system
- Appointment scheduling
- Health tracking and logs
- Billing and payments
- Team management
- Compliance reporting
- Real-time notifications

## Support

For deployment issues, check:
1. Error logs in PythonAnywhere
2. Django debug toolbar (in development)
3. Console output during deployment

## Security Notes

- Change SECRET_KEY in production
- Use HTTPS in production
- Set DEBUG=False
- Configure proper ALLOWED_HOSTS
- Use environment variables for sensitive data
