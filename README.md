# WeekPlanner

# WeekPlanner

A minimal Django app for navigating through daily task pages, showcasing simple routing and template rendering.

# 🛠️ Initialize

## Step 1: Create project and app

django-admin startproject weekplanner
cd weekplanner
python manage.py startapp tasks

## Step 2: weekplanner/settings.py

INSTALLED_APPS = [
...
'tasks',
]

## Step 3: Place HTML files inside

tasks/templates/tasks/

## Step 4: tasks/views.py

from django.shortcuts import render

def index(request):
return render(request, 'tasks/index.html')

def monday(request):
return render(request, 'tasks/monday.html')

### ...similarly for other days

## Step 5: tasks/urls.py

from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('monday/', views.monday, name='monday'),

### ...add more days here

]

## Step 6: weekplanner/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
path('admin/', admin.site.urls),
path('tasks/', include('tasks.urls')),
]

## Step 7: requirements.txt

Django>=3.2,<4
gunicorn

## Step 8: weekplanner/settings.py

ALLOWED_HOSTS = ['weekplanner-zntz.onrender.com']

# 🚀 Run Dev

## Create virtual environment at root level

python -m venv .venv

## Activate virtual environment

.venv\Scripts\activate # For Windows
source .venv/bin/activate # For macOS/Linux

## Run development server

python manage.py runserver
