from django.conf import settings
from django.core.cache import cache

from diary.models import Entry


def get_cache_for_entries_count():
    if settings.CACHE_ENABLED:
        key = "entries_count"
        entries_count = cache.get(key)
        if entries_count is None:
            entries_count = Entry.objects.all().count()
            cache.set(key, entries_count)
    else:
        entries_count = Entry.objects.all().count()
    return entries_count
