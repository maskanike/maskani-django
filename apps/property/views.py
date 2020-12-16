from django.shortcuts import render

from .forms import PropertyForm

def properties(request):
    form = PropertyForm()
    return render(request, 'properties.html', {'form': form })