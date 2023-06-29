# Generated by Django 4.2.2 on 2023-06-29 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_date', models.DateTimeField(auto_now=True)),
                ('site_name', models.TextField(max_length=200, verbose_name='Имя')),
                ('site_phone', models.TextField(max_length=200, verbose_name='Телефон')),
                ('site_time', models.TextField(max_length=200, verbose_name='Время')),
                ('site_day', models.DateField()),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.DeleteModel(
            name='SiteTable',
        ),
    ]
