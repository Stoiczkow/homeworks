from django.http import HttpResponse


def user_view(request, username):
    return HttpResponse(f"<h1> Witaj na profilu {username}</h1>")