from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from diary.forms import EntryForm
from diary.models import Entry


class Index(TemplateView):
    model = Entry
    template_name = "diary/index.html"


class EntryListView(LoginRequiredMixin, ListView):
    model = Entry
    context_object_name = "entry_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("query", "")
        return context


class EntryCreateView(LoginRequiredMixin, CreateView):
    model = Entry
    form_class = EntryForm
    success_url = reverse_lazy("diary:entry_list")
    extra_context = {"title": "Create entry"}

    def form_valid(self, form):
        new_entry = form.save(commit=False)
        new_entry.owner = self.request.user
        new_entry.save()
        return super().form_valid(form)


class EntryDetailView(LoginRequiredMixin, DetailView):
    model = Entry


class EntryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Entry
    form_class = EntryForm
    success_url = reverse_lazy("diary:entry_list")
    extra_context = {"title": "Edit entry"}

    def test_func(self):
        entry = self.get_object()
        if self.request.user.is_staff:
            return True
        return self.request.user == entry.owner


class EntryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy("diary:entry_list")

    def test_func(self):
        entry = self.get_object()
        if self.request.user.is_superuser:
            return True
        return self.request.user == entry.owner


@login_required
def entry_search(request):
    query = request.GET.get("query", "")
    if query:
        search_list = Entry.objects.filter(
            title__icontains=query
        ) | Entry.objects.filter(text__icontains=query)
    else:
        search_list = Entry.objects.none()
    return render(
        request, "diary/entry_list.html", {"entry_list": search_list, "query": query}
    )
