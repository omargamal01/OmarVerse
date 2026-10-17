# Omar Gamal Portfolio — Django

## Run locally (Windows PowerShell)
1. Install Python 3.11 or newer.
2. Extract this ZIP and open PowerShell in this folder.
3. Run:
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Website: http://127.0.0.1:8000/  
Admin dashboard: http://127.0.0.1:8000/admin/

Add/edit/delete projects from the admin dashboard. Each project supports a category, description, technology tags, image, attachment, GitHub URL, project URL, and featured/published toggles.

## Deployment
Set DJANGO_SECRET_KEY, DJANGO_DEBUG=False, and DJANGO_ALLOWED_HOSTS on your host. Configure persistent media storage for uploaded files, a production database if available, HTTPS, and email settings before going live. This is a ready-to-run project package, not a website already hosted publicly.
