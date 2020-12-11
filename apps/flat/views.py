from django.shortcuts import render

from .forms import FlatForm

def flats(request):
    form = FlatForm()
    return render(request, 'flats.html', {'form': form })