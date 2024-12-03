from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': 'True', 'blank': 'True'}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    avatar = models.ImageField(upload_to='user_pictures/', verbose_name='Avatar', **NULLABLE)
    verification_code = models.CharField(max_length=10, verbose_name='Verification_code', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ('email',)
