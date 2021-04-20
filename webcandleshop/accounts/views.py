from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
 
 
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST) # Создание объекта формы с данными 
        if form.is_valid():
            """ Проверка валидности """
            cd = form.changed_data
            user = authenticate(request,
                                username=cd[0], 
                                password=cd[0])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Успешная аутентификация')
                else:
                    return HttpResponse('Некорректный логин или пароль')
        else:
            return HttpResponse('Введите корректные данные')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    pass