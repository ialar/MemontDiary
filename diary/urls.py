from django.urls import path

from diary.apps import DiaryConfig
from diary.views import Index, EntryListView, EntryCreateView, EntryUpdateView, EntryDetailView, EntryDeleteView

app_name = DiaryConfig.name

urlpatterns = [
    path("", Index.as_view(), name='index'),
    path('entries/', EntryListView.as_view(), name='entry_list'),
    path('entry/create/', EntryCreateView.as_view(), name='entry_create'),
    path('entry/update/<int:pk>/', EntryUpdateView.as_view(), name='entry_update'),
    path('entry/detail/<int:pk>/', EntryDetailView.as_view(), name='entry_detail'),
    path('entry/<int:pk>/', EntryDeleteView.as_view(), name='entry_delete'),
]
