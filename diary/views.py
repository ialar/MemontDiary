from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView

from diary.forms import EntryForm
from diary.models import Entry
from diary.services import get_current_date


class Index(TemplateView):
    model = Entry
    template_name = 'diary/index.html'
    # extra_context = {'title': 'Memont diary'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formatted_current_date'] = get_current_date()
        return context


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
