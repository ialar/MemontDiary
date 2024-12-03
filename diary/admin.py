from django.contrib import admin

from diary.models import Entry


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'created_at', 'is_public', 'owner')
    list_filter = ('title', 'created_at')
    search_fields = ('title', 'text')
