from django.shortcuts import render


def home(request):
    return render(request, 'menus/index.html')


def page_view(request, slug):
    return render(request, 'menus/index.html')
