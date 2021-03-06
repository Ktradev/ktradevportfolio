from django.shortcuts import render

from .models import Skill

# Create your views here.
def profile(request):
	context = {
		'skills': Skill.objects.all().order_by('-id')
	}
	return render(request, 'profile/profile.html', context)