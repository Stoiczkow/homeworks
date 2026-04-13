from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Note
from .forms import NoteForm


def all_notes(request):
    notes_list = Note.objects.all()
    paginator = Paginator(notes_list, 3)  # 3 notes per page
    page = request.GET.get('page')
    try:
        notes = paginator.page(page)
    except PageNotAnInteger:
        notes = paginator.page(1)
    except EmptyPage:
        notes = paginator.page(paginator.num_pages)
    return render(request, "notatnik/notes.html", {"notes": notes})


def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, "notatnik/note_detail.html", {"note": note})


def add_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return redirect("note_detail", note_id=note.id)
    else:
        form = NoteForm()
    return render(request, "notatnik/note_form.html", {"form": form})
 