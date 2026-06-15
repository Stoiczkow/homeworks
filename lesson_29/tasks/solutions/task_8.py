'''
Napisz zadanie, które symuluje przetwarzanie wideo przez 15 sekund (time.sleep(15)).
Widok, który je wywołuje, powinien natychmiast zwrócić komunikat "Przetwarzanie wideo
rozpoczęte!"
'''

import time
from celery import shared_task

@shared_task
def process_video():
    print("Start przetwarzania wideo...")
    time.sleep(15)
    print("Przetwarzanie wideo zakończone!")
    return "done"
