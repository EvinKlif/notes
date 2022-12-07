from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView
from .forms import AddNoteForm
from .models import Notes
from .utils import DataMixin


class CreateNote(DataMixin, CreateView):
    form_class = AddNoteForm
    template_name = 'note/create-note.html'

    def get_form_kwargs(self):
        """Adding a user id to a note when it is created."""
        kwargs = super(CreateNote, self).get_form_kwargs()
        if kwargs['instance'] is None:
            kwargs['instance'] = Notes()
        kwargs['instance'].user = self.request.user
        return kwargs


class ShowNote(DataMixin, DetailView):
    """Displaying the selected note."""
    model = Notes
    template_name = 'note/view-note.html'
    slug_url_kwarg = 'note_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(ShowNote, self).get_context_data(**kwargs)
        context['list'] = Notes.objects.filter(user_id=self.request.user)
        return context




class AllNotes(DataMixin, ListView):
    model = Notes
    template_name = 'note/notes.html'
    slug_url_kwarg = 'note_slug'
    context_object_name = 'posts'

    def get_queryset(self):
        return Notes.objects.filter(user_id=self.request.user)


class UpdateNote(DataMixin, UpdateView):
    """Update the selected note."""
    model = Notes
    form_class = AddNoteForm
    template_name = 'note/create-note.html'
    slug_url_kwarg = 'note_slug'
    context_object_name = 'post'


class DeleteNote(DataMixin, DeleteView):
    """Deleting the selected note."""
    model = Notes
    slug_url_kwarg = 'note_slug'

    def get_success_url(self):
        return reverse_lazy('notes')
