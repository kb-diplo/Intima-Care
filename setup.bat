@echo off
echo.
echo ========================================
echo   IntimaCare Django Project Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python and try again
    pause
    exit /b 1
)

REM Check if manage.py exists
if not exist "manage.py" (
    echo Error: manage.py not found
    echo Please run this script from the project root directory
    pause
    exit /b 1
)

echo Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo Warning: Failed to install some dependencies
    echo You may need to install them manually
)

echo.
echo Creating migrations...
python manage.py makemigrations

echo.
echo Running migrations...
python manage.py migrate

echo.
echo Loading sample data...
python manage.py loaddata sample_data.json
if errorlevel 1 (
    echo Sample data loading failed, trying alternative method...
    python manage.py setup_initial_data
)

echo.
echo Collecting static files...
python manage.py collectstatic --noinput

echo.
echo ========================================
echo           Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Create a superuser: python manage.py createsuperuser
echo 2. Start the server: python manage.py runserver
echo 3. Visit http://127.0.0.1:8000 to view the website
echo 4. Visit http://127.0.0.1:8000/admin for admin panel
echo.
echo Don't forget to:
echo - Upload a logo in the admin panel
echo - Customize the site settings
echo - Add your own content and images
echo.
pause
