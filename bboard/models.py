from django.db import models
from django.utils import timezone


class Bb(models.Model):
   title = models.CharField(max_length=50, verbose_name='Товар')
   content = models.TextField(verbose_name='Описание')
   price = models.FloatField(verbose_name='Цена')
   publish = models.DateTimeField(default=timezone.now, db_index=True, verbose_name='Опубликовано')
   rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

   class Meta:
      verbose_name_plural = 'Объявления'
      verbose_name = 'Объявление'
      ordering = ['-publish']


class Rubric(models.Model):
   name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

   class Meta:
      verbose_name_plural = 'Рубрики'
      verbose_name = 'Рубрика'
      ordering = ['name']

   def __str__(self):
      return self.name