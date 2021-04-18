from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm


def index(request):
	return render(request, 'registration/index.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():		# Если форма заполнена правильно
            form.save()		# Создаем пользователя
            username = form.cleaned_data.get('username')	# с именем
            raw_password = form.cleaned_data.get('password1')# и паролем
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home.index') #страница редиректа после регистрации
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})