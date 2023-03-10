# Generated by Django 4.1.7 on 2023-02-20 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('name', models.CharField(help_text='Поле для имени комнаты',
                                          max_length=30,
                                          verbose_name='Название комнаты')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
