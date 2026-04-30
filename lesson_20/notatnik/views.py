from django.shortcuts import render
from .models import Note
from django.core.paginator import Paginator
# Create your views here.

#task6
def show_Note(request):
    notes_list = Note.objects.all()
    return render(request, "notes/all_notes.html", {'notes' : notes_list})

def show_One_Note(request, note_id):
    note = Note.objects.filter(id=note_id).first()
    if note is None:
        note = Note.objects.all().last()
    return render(request, "notes/one_note.html", {'notes' : note})



#task10
def paginacja(request):
    all_Notes = Note.objects.all().order_by('-id')
    paginator = Paginator(all_Notes, 3)


    page_number = request.GET.get('paginacja')
    object = paginator.get_page(page_number)
    return render(request, 'notes/paginator.html', {'page_obj':object})