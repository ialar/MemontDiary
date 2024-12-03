from django.db import models
from django.utils import timezone

from config import settings

NULLABLE = {'null': 'True', 'blank': 'True'}
USER = settings.AUTH_USER_MODEL


class Entry(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    text = models.TextField(verbose_name='Text')
    image = models.ImageField(upload_to='diary_images/', verbose_name='Image', **NULLABLE)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Date')
    is_public = models.BooleanField(default=False, verbose_name="Public")
    owner = models.ForeignKey(USER, on_delete=models.SET_NULL, verbose_name='Owner', **NULLABLE)

    # tag = models.CharField(max_length=50, verbose_name='Tag', **NULLABLE)

    def __str__(self):
        return f'"{self.title}" (added: {self.created_at})'

    class Meta:
        verbose_name = 'entry'
        verbose_name_plural = 'entries'
        ordering = ('created_at',)


# class Comment(models.Model):
#     entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name='comments')
#     text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'Comment on {self.entry}: {self.text[:20]}...'
