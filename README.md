# weekplanner

A Django app to view weekly tasks exhibiting routing between pages.

**Initialze**
**1**
django-admin startproject {weekplanner}
python manage.py startapp tasks

**2**
weekplanner/settings.py:
INSTALLED_APPS = [
'tasks',
]

**3**
All webpages are stored in tasks/templates/tasks

**4**
configure tasks/views.py
from django.shortcuts import render

**5**
def index(request):
return render(request, 'tasks/index.html') .. and so on.
This creates render functions for requesting webpages when called.

**6**
tasks/urls.py
from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name='index'),
path('monday/', views.monday, name='monday'),
.. and so on
] -- connects the urls{webpage} to views{directory}

**7**
weekplanner/urls.py
urlpatterns = [
path('tasks/', include('tasks.urls')),
] -- imports all the urls from tasks.urls and serves them tasks/{url}/

**8**
requirements.txt
Django>=3.2,<4 --for installing
gunicorn --for deployement

**9**
Adding allowed hosts to deploy on <a>weekplanner-zntz.onrender.com</a>
