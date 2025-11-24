# IntimaCare - Telehealth Platform

A comprehensive Django-based telehealth platform with CMS functionality, branding management, and multiple website pages.

## Features

- **CMS System**: Admin-managed content for all pages
- **Branding Management**: Logo and theme color management
- **Responsive Design**: Modern, clean UI with IntimaCare branding
- **Multiple Pages**: Home, About, Services, Contact, FAQ, Legal documents
- **Contact Form**: Stores messages in admin panel
- **Dynamic Content**: Homepage sections, FAQs, and service features managed through admin

## Theme Colors

- **Primary**: Yellow (#FFC300)
- **Secondary**: Black (#000000)
- **Background**: White (#FFFFFF)

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Superuser

```bash
python manage.py createsuperuser
```

### 4. Load Sample Data (Optional)

```bash
python manage.py loaddata sample_data.json
```

### 5. Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to view the website and `http://127.0.0.1:8000/admin` for the admin panel.

## Project Structure

```
intimacare/
├── intimacare/          # Main project settings
├── core/                # Public website pages
├── cms/                 # Content Management System
├── branding/            # Branding and theme management
├── templates/           # HTML templates
├── static/              # CSS, JS, images
└── media/               # User uploaded files
```

## Apps Overview

### Core App
- **Purpose**: Public website pages and views
- **Templates**: Home, About, Services, Contact, FAQ, Legal documents
- **Features**: Contact form handling, page routing

### CMS App
- **Purpose**: Content management system
- **Models**: SiteSettings, HomepageSection, FAQ, LegalDocument, ContactMessage, ServiceFeature
- **Features**: Admin interface for all content management

### Branding App
- **Purpose**: Theme and branding management (integrated into CMS)
- **Features**: Logo upload, color scheme management

## Admin Features

### Site Settings
- Site name and tagline
- Logo upload
- Primary/secondary colors
- Contact information
- About text, mission, vision

### Homepage Management
- Dynamic homepage sections
- Image uploads
- Content ordering
- Active/inactive toggle

### FAQ Management
- Question and answer pairs
- Ordering and activation
- Admin-friendly interface

### Legal Documents
- Privacy Policy
- Terms & Conditions
- Cookies Policy
- Accessibility Statement

### Contact Messages
- View all contact form submissions
- Mark as read/unread
- Search and filter capabilities

### Service Features
- Manage platform service features
- Icon class support
- Ordering and activation

## Customization

### Adding New Pages
1. Create view in `core/views.py`
2. Add URL pattern in `core/urls.py`
3. Create template in `core/templates/core/`

### Modifying Styles
- Edit `static/css/main.css`
- Colors are defined as CSS variables in `:root`
- Responsive breakpoints included

### Adding New CMS Models
1. Add model to `cms/models.py`
2. Register in `cms/admin.py`
3. Run migrations
4. Update templates as needed

## Production Deployment

1. Set `DEBUG = False` in settings
2. Configure `ALLOWED_HOSTS`
3. Set up proper database (PostgreSQL recommended)
4. Configure static file serving
5. Set up media file handling
6. Use environment variables for sensitive settings

## Support

For questions or issues, please contact the development team or refer to the Django documentation.

## License

This project is proprietary to IntimaCare.
