from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

#from .forms import RegisterForm

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
	else:
		form = UserCreationForm()

	return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    # Redirect to a success page.
	


