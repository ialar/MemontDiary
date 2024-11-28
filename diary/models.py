from django.db import models
from django.utils import timezone

NULLABLE = {'null': 'True', 'blank': 'True'}


class Entry(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    text = models.TextField(verbose_name='Text')
    image = models.ImageField(upload_to='diary_images/', verbose_name='Image', **NULLABLE)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Date')
    is_public = models.BooleanField(default=False, verbose_name="Public")

    def __str__(self):
        return f'"{self.title}" (added: {self.created_at})'

    class Meta:
        verbose_name = 'entry'
        verbose_name_plural = 'entries'
        ordering = ('created_at',)
