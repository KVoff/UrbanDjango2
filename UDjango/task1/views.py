from django.shortcuts import render
from .forms import UserRegister
from .models import Game, Buyer


def shop_template(request):
    # Получаем все записи из модели Game
    games = Game.objects.all()
    context = {
        'games': games,
    }
    return render(request, 'shop.html', context)


def shoppingcart(request):
    return render(request, 'shoppingcart.html')


def sign_up_by_html(request):
    info = {}
    username = ''
    age = ''

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        age = request.POST.get('age')

        try:
            age = int(age)
        except ValueError:
            info['error'] = 'Возраст должен быть числом'
        else:
            if password != confirm_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif Buyer.objects.filter(name=username).exists():
                info['error'] = 'Пользователь уже существует'
            else:
                # Добавляем пользователя в список
                Buyer.objects.create(name=username, age=age)
                return render(request,
                              'welcome.html',
                              {'username': username})

    if request.method == 'GET':
        info = {}

    return render(request,
                  'registration_page.html',
                  {'info': info, 'username': username, 'age': age})


def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            age = form.cleaned_data['age']

            if password != confirm_password:
                form.add_error('confirm_password', 'Пароли не совпадают')
            elif age < 18:
                form.add_error('age', 'Вы должны быть старше 18')
            elif Buyer.objects.filter(name=username).exists():
                form.add_error('username', 'Пользователь уже существует')
            else:
                # Добавляем пользователя в список
                Buyer.objects.create(name=username, age=age)
                return render(request,
                              'welcome.html',
                              {'username': username}
                              )
    else:
        form = UserRegister()

    return render(request,
                  'registration_page.html',
                  {'form': form})

