from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
	if (request.user.profile.role==1):
		return render(request, 'student/profile.html')
	elif (request.user.profile.role==2):
		return render(request, 'teacher/profile.html')
	else:
		return render(request, 'principal/profile.html')	