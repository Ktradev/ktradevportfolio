from django.shortcuts import render

from timeline.models import Panel

# Create your views here.
def library(request, id):
	context = {
		'id': id,
		'panel': Panel.objects.get(id = id)
	}
	return render(request, 'library/library.html', context)