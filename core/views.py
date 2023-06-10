from django.shortcuts import render
from items.models import Item

def index(request):
    return render(request, 'core/index.html')

def schedule(request):
    return render(request, 'core/schedule.html')
def lecture(request):
    items = Item.objects.all()

    return render(request, 'core/lecture.html', {'all_items': items})