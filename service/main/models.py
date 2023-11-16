from django.db import models

from users.models import CustomUser


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title


class Application(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    image = models.ImageField(upload_to='images/', verbose_name='Фото помещения или план')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Владелец')

    def __str__(self):
        return self.title
