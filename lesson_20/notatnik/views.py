from django.views.generic import DetailView, ListView

from notatnik.models import Notatnik

class ListaNotatekView(ListView):
    model = Notatnik
    template_name = 'notatnik.html'
    context_object_name = 'notatki'


class NoteDetailView(DetailView):
    model = Notatnik
    template_name = 'notatka.html'
