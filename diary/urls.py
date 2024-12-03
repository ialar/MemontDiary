from django.urls import path
from django.views.decorators.cache import cache_page

from diary.apps import DiaryConfig
from diary.views import Index, EntryListView, EntryCreateView, EntryUpdateView, EntryDetailView, EntryDeleteView, \
    entry_search

app_name = DiaryConfig.name

urlpatterns = [
    path("", Index.as_view(), name='index'),
    path('entries/', EntryListView.as_view(), name='entry_list'),
    path('entry/create/', EntryCreateView.as_view(), name='entry_create'),
    path('entry/update/<int:pk>/', EntryUpdateView.as_view(), name='entry_update'),
    path('entry/detail/<int:pk>/', cache_page(30)(EntryDetailView.as_view()), name='entry_detail'),
    path('entry/delete/<int:pk>/', EntryDeleteView.as_view(), name='entry_delete'),
    path('search/', entry_search, name='entry_search'),
]
