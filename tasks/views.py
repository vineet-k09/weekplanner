from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'tasks/index.html')

def monday(request):
    return render(request, 'tasks/monday.html')

def tuesday(request):
    return render(request, 'tasks/tuesday.html')

def wednesday(request):
    return render(request, 'tasks/wednesday.html')

def thursday(request):
    return render(request, 'tasks/thursday.html')

def friday(request):
    return render(request, 'tasks/friday.html')

def saturday(request):
    return render(request, 'tasks/saturday.html')

def sunday(request):
    return render(request, 'tasks/sunday.html')
