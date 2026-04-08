from django.shortcuts import render
from django.http import HttpResponse
from .models import Note

# Create your views here.

def all_notes(request):
    notes = Note.objects.all()
    
    return render(request, 'notes.html', {'notes': notes}) 

def one_note(request, note_id):
    note = Note.objects.get(id=note_id)
    return HttpResponse(f"{note.title} <br> {note.content}")