from django.http import JsonResponse
from django.shortcuts import render

from tasks.solutions.task_8 import process_video
from tasks.solutions import task_1
from tasks.solutions.task_2 import multiply
from tasks.solutions.task_3 import save_timestamp
from tasks.solutions.task_5 import count_users
from tasks.solutions.task_7 import update_user_last_login

# Zadanie 1 - hallo world
def generate_console_text_view(request):
    task = task_1.deley(2)
    return JsonResponse({"message": "Przetwarzanie zadania...", "id": task.id})


# Zadanie 2
def multiply_view(request):
    context_data = {}
    if request.method == 'POST':
        try:
            a = float(request.POST.get('a', ''))
            b = float(request.POST.get('b', ''))
        except ValueError:
            context_data['error'] = 'Wpisz dwie liczby.'
            return render(request, 'multiply.html', context_data)

        calc_result = multiply.delay(a, b)
        try:
            result = calc_result.get(timeout=7)
        except Exception as exc:
            context_data['error'] = f'Wystąpił błąd: {exc}'
            context_data.update({'id': calc_result.id, 'a': a, 'b': b})
            return render(request, 'tasks/solutions/multiply.html', context_data)

        context_data.update({
            'a': a, 'b': b,
            'id': calc_result.id,
            'result': result,
        })
    return render(request, 'multiply.html', context_data)


# Zadanie 3
def save_timestamp_view(request):
    task = save_timestamp.delay()
    return JsonResponse({
        "message": "Dopisano timestamp do log.txt.",
        "task_id": task.id,
    })


# Zadanie 5
def count_users_view(request):
    task = count_users.delay()
    return JsonResponse({
        "message": "Zadanie liczenia użytkowników rozpoczęte...",
        "id": task.id,
    })

# Zadanie 7
def update_user_last_login_view(request, user_id):
    task = update_user_last_login.delay(user_id)
    return JsonResponse({
        "message": f"Zadanie 7 - user_id={user_id}",
        "id": task.id,
    })


# Zadanie 8
def start_video_processing(request):
    process_video.delay()
    return JsonResponse({"message": "Przetwarzanie wideo rozpoczęte!"})
