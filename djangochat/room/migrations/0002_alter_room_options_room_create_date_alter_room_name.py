# Generated by Django 4.1.7 on 2023-02-20 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ('-create_date',), 'verbose_name': 'Группа',
                     'verbose_name_plural': 'Группы'},
        ),
        migrations.AddField(
            model_name='room',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(help_text='Поле для имени комнаты',
                                   max_length=50,
                                   verbose_name='Название комнаты'),
        ),
    ]
