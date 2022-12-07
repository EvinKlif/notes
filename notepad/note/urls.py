from django.urls import path

from .views import *

urlpatterns = [

    path('create-note/', CreateNote.as_view(), name='add_note'),
    path('note/<slug:note_slug>/', ShowNote.as_view(), name='show_note'),
    path('notes/', AllNotes.as_view(), name='notes'),
    path('update/<slug:note_slug>/', UpdateNote.as_view(), name='update'),
    path('del/<slug:note_slug>/', DeleteNote.as_view(), name='delete'),
]
