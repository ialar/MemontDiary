from django.urls import path

from diary.apps import DiaryConfig
from diary.views import index

app_name = DiaryConfig.name

urlpatterns = [
    path('', index, name='index')
]
