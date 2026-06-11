from django.http import HttpResponse


def info_view(request):
    return HttpResponse("<h1> Informacja o stronie</h1>")
