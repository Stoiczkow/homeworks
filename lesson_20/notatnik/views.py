from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Note

# Create your views here.
def show_notes(request):
    all_notes = Note.objects.all()
    
    paginator = Paginator(all_notes, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, "notes.html", {"page_obj": page_obj})


def show_note_details(request, note_id):
    note = Note.objects.get(id=note_id)
    
    return render(request, "note_details.html", {'note': note})