from django.shortcuts import render


def index(request):
    context = {"carousel": "carousel"}

    return render(request, "theme/home_page.html", context)
