from django.shortcuts import render


def search(request):
    return render(request, 'products/search.html')


def show_results(request):
    pass
