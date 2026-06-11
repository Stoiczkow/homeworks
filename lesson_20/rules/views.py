from django.http import HttpResponse


def rules_view(request):
    return HttpResponse("<h1> Regulamin </h1>")
