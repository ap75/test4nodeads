from django.db import models
from django.utils import timezone

class Group(models.Model):
    parent = models.ForeignKey('api.Group', on_delete=models.CASCADE, null=True, blank=True,
        related_name='group_parent', verbose_name='Родительская группа')
    icon = models.ImageField('Иконка', upload_to='upload')
    name = models.CharField('Название', max_length=64, unique=True)
    descr = models.TextField('Описание', max_length=512, null=True, blank=True)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name


class Element(models.Model):
    group = models.ForeignKey('api.Group', on_delete=models.CASCADE,
        related_name='element_group', verbose_name='Родительская группа')
    icon = models.ImageField('Иконка', upload_to='upload')
    name = models.CharField('Название', max_length=64, unique=True)
    descr = models.TextField('Описание', max_length=512, null=True, blank=True)
    created = models.DateField('Дата создания', default=timezone.now)
    checked = models.NullBooleanField('Проверен модератором')

    class Meta:
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'

    def __str__(self):
        return self.name
