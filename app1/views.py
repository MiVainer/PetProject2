from django.shortcuts import render

def index(request):
    # Мы уже в папке templates, указываем путь к нашему файлу главной страницы c использованием метода render
    data = {
        'title': 'Главная страница',
        'values': ['One', 'Two', 'Three']

    }
    return render(request, 'app1/index.html', data)

def about(request):
    return render(request, 'app1/about.html')

def contacts(request):
    return render(request, 'app1/contacts.html')