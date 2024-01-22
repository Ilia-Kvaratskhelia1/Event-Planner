from django.shortcuts import render
from django.http import HttpResponse
from .models import Events
# Create your views here.

def index(request):
    all_events = Events.objects.all()
    return render(request, 'index.html', {'events':all_events})

def events_detail(request, title):
    events = Events.objects.get(title = title)
    
    return render(request, 'events_detail.html/', {'events':events})

