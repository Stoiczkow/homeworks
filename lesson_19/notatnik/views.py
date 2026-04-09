from django.shortcuts import render
from .models import Note
from django.core.paginator import Paginator

# Create your views here.
def show_all_notes(request):
    
    all_notes = Note.objects.all()
    paginator = Paginator(all_notes, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'all_notes.html', {"page_obj": page_obj})

def show_note(request, note_id):

    try:
        note = Note.objects.get(id=note_id)
    except:
        return render(request, 'note.html', {"message": f"Wystąpił błąd podczas pobierania danych o notatce ID {note_id}"})

    return render(request, 'note.html', {"note": note})