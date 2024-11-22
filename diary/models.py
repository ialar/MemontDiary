from django.db import models
from django.utils import timezone

NULLABLE = {'null': 'True', 'blank': 'True'}


class Entry(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст записи')
    image = models.ImageField(upload_to='diary_images/', verbose_name='Изображение', **NULLABLE)
    created_at = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')

    def __str__(self):
        return f'"{self.title}" (дата создания: {self.created_at})'

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
        ordering = ('created_at',)
