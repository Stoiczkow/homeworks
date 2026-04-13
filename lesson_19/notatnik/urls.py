from django.urls import path
from .views import all_notes, note_detail, add_note

urlpatterns = [
    path('notes/', all_notes, name='notes_list'),
    path('notes/add/', add_note, name='note_add'),
    path('notes/<int:note_id>/', note_detail, name='note_detail'),
]
