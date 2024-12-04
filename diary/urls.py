from django.urls import path
from django.views.decorators.cache import cache_page

from diary.apps import DiaryConfig
from diary.views import (EntryCreateView, EntryDeleteView, EntryDetailView,
                         EntryListView, EntryUpdateView, Index, EntrySearchView)

app_name = DiaryConfig.name

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("entries/", EntryListView.as_view(), name="entry_list"),
    path("entry/create/", EntryCreateView.as_view(), name="entry_create"),
    path("entry/update/<int:pk>/", EntryUpdateView.as_view(), name="entry_update"),
    path(
        "entry/detail/<int:pk>/",
        cache_page(30)(EntryDetailView.as_view()),
        name="entry_detail",
    ),
    path("entry/delete/<int:pk>/", EntryDeleteView.as_view(), name="entry_delete"),
    path("search/", EntrySearchView.as_view(), name="entry_search"),
]
