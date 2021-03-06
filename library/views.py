from django.shortcuts import render

from profile.models import Skill

# Create your views here.
def library(request, id):
	context = {
		'id': id,
		'skill': Skill.objects.get(id = id)
	}
	return render(request, 'library/library.html', context)