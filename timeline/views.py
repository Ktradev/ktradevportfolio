from django.shortcuts import render

from .models import Panel, Timestamp, Date

# Create your views here.
def timeline(request):
	context = {
		'dates': Date.objects.all().order_by('-id'),
		'timestamps': Timestamp.objects.all().order_by('-id'),
		'panels': Panel.objects.all().order_by('-id')
	}
	return render(request, 'timeline/timeline.html', context)