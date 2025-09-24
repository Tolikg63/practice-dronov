from django.db import models


class Bb(models.Model):
   title = models.CharField(max_length=50, verbose_name='Товар')
   content = models.TextField(verbose_name='Описание')
   price = models.FloatField(verbose_name='Цена')
   publish = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')


   def __str__(self):
      return self.title
   

   class Meta:
      verbose_name_plural = 'Объявления'
      verbose_name = 'Объявление'
      ordering = ['-publish']