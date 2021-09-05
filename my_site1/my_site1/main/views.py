from django.shortcuts import render


# # Вывводим небольшие кусочки текста через класс HttpResponse
def index(request):
    data = {
        'title': 'Главная страница'
    }
    # метод принимает request и html шаблон
    # стартуем из созданной папки templates и пишем путь до html файла
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, "main/about.html")


def contacts(request):
    return render(request, "main/contacts.html")