from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# sign up function
def signup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			#log user in
			login(request, user)
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(request, 'accounts/signup.html', {'form':form})

# login function
def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			#login in the user
			user = form.get_user()
			login(request, user)
			return redirect('home')
	else:
		form = AuthenticationForm()
	return render(request, 'accounts/login.html', {'form': form})

#logout function
def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect('home')