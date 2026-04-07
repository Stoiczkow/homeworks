from django.shortcuts import render
from django.views.generic import ListView, DetailView

from note.models import Note


# Create your views here.
class NoteListView(ListView):
    model = Note
    template_name = 'note.html'
    context_object_name = 'notes'
    paginate_by = 3


class NoteDetailView(DetailView):
    model = Note
    template_name = 'note_detail.html'

