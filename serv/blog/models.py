from django.db import models

class Blog(models.Model):
    site_date = models.DateTimeField(auto_now=True)
    site_name = models.TextField(max_length=50, verbose_name='Имя')
    site_phone = models.TextField(max_length=50, verbose_name='Телефон')
    site_time = models.TextField(max_length=50, verbose_name='Время')
    site_day = models.DateField(verbose_name='День')





    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


