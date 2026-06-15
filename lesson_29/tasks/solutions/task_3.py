'''
Stwórz zadanie log_timestamp(), które zapisuje aktualną datę i godzinę do pliku log.txt
'''

from datetime import datetime

from celery import shared_task


@shared_task
def save_timestamp():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(timestamp + '\n')
    return timestamp