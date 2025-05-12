# WeekPlanner

# WeekPlanner

A minimal Django app for navigating through daily task pages, showcasing simple routing and template rendering.

# 🛠️ Initialize

## Step 1: Create project and app

```bash
django-admin startproject weekplanner
cd weekplanner
python manage.py startapp tasks
```

## Step 2: weekplanner/settings.py

```python
INSTALLED_APPS = [
'tasks',
]
```

## Step 3: Place HTML files inside

tasks/templates/tasks/

## Step 4: tasks/views.py

```python
from django.shortcuts import render

def index(request):
return render(request, 'tasks/index.html')

def monday(request):
return render(request, 'tasks/monday.html')
```

### ...similarly for other days

## Step 5: tasks/urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('monday/', views.monday, name='monday'),
...add more days here
]
```

## Step 6: weekplanner/urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
path('admin/', admin.site.urls),
path('tasks/', include('tasks.urls')),
]
```

## Step 7: requirements.txt

Django>=3.2,<4
gunicorn

## Step 8: weekplanner/settings.py

```ALLOWED_HOSTS = ['weekplanner-zntz.onrender.com']```

# 🚀 Run Dev

## Create virtual environment at root level

`python -m venv .venv`

## Activate virtual environment

```.venv\Scripts\activate```

## Run development server

(.venv) python manage.py runserver

`pip install django` -- incase shows module not found
technically it should

# 👀 Adding styles

weekplanner/static/css/styles.css

### settings.py

```python
STATIC_URL = 'static/'

STATICFILES_DIRS = [
BASE_DIR / "static", # This points to the static directory
]
```

## Styles config for serving thru Render

### settings.py

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
```

`python manage.py collectstatic` -- before each deployment it seems

### settings.py

```python
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ... the rest
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

`pip install whitenoise` -- WhiteNoise lets Django serve static files without needing Nginx or some external server.

### To autogenerate requirements.txt

`pip freeze > requirements.txt`

## Procfile

Tell your platform how to run your app
Put this file in your root directory (no extension), and inside write:

`web: gunicorn weekplanner.wsgi:application`
