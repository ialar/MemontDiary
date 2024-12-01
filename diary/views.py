from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView

from diary.forms import EntryForm
from diary.models import Entry


class Index(TemplateView):
    model = Entry
    template_name = 'diary/index.html'
    # extra_context = {'title': 'Memont diary'}


class EntryListView(ListView):
    model = Entry
    # extra_context = {'title': 'List of entries'}


class EntryCreateView(CreateView):
    model = Entry
    form_class = EntryForm
    success_url = reverse_lazy('diary:entry_list')
    extra_context = {'title': 'Create entry'}


class EntryDetailView(DetailView):
    model = Entry


class EntryUpdateView(UpdateView):
    model = Entry
    form_class = EntryForm
    success_url = reverse_lazy('diary:entry_list')
    extra_context = {'title': 'Edit entry'}


class EntryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy('diary:entry_list')
