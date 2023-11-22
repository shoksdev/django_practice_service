from django.db import models

from users.models import CustomUser


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title


class Application(models.Model):
    STATUS_CHOICES = [
        ('Н', 'Новая'),
        ('П', 'Принято в работу'),
        ('В', 'Выполнено')
    ]
    created = models.DateTimeField(auto_now_add=True, verbose_name='Временная метка')
    title = models.CharField(max_length=80, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    image = models.ImageField(upload_to='images/', verbose_name='Фото помещения или план')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0], verbose_name='Статус')
    image_created = models.ImageField(upload_to='images_created/', verbose_name='Созданный дизайн', blank=True)
    comment = models.TextField(verbose_name='Комментарий', blank=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Владелец')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title
