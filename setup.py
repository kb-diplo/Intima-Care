#!/usr/bin/env python
"""
IntimaCare Setup Script
Run this script to quickly set up the IntimaCare Django project
"""

import os
import sys
import subprocess

def run_command(command, description):
    """Run a command and print status"""
    print(f"\n🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def main():
    print("🚀 IntimaCare Django Project Setup")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists('manage.py'):
        print("❌ Error: manage.py not found. Please run this script from the project root directory.")
        sys.exit(1)
    
    # Install dependencies
    if not run_command("pip install -r requirements.txt", "Installing dependencies"):
        print("⚠️  You may need to install dependencies manually: pip install -r requirements.txt")
    
    # Make migrations
    run_command("python manage.py makemigrations", "Creating migrations")
    
    # Run migrations
    run_command("python manage.py migrate", "Running migrations")
    
    # Load sample data
    if run_command("python manage.py loaddata sample_data.json", "Loading sample data"):
        print("✅ Sample data loaded successfully")
    else:
        # Fallback to management command
        run_command("python manage.py setup_initial_data", "Setting up initial data")
    
    # Collect static files
    run_command("python manage.py collectstatic --noinput", "Collecting static files")
    
    print("\n🎉 Setup Complete!")
    print("=" * 50)
    print("Next steps:")
    print("1. Create a superuser: python manage.py createsuperuser")
    print("2. Start the development server: python manage.py runserver")
    print("3. Visit http://127.0.0.1:8000 to view the website")
    print("4. Visit http://127.0.0.1:8000/admin to access the admin panel")
    print("\n📝 Don't forget to:")
    print("- Upload a logo in the admin panel")
    print("- Customize the site settings")
    print("- Add your own content and images")

if __name__ == "__main__":
    main()
