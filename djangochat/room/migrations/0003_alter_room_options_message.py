import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('room', '0002_alter_room_options_room_create_date_alter_room_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ('-create_date',), 'verbose_name': 'Комната',
                     'verbose_name_plural': 'Комнаты'},
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('content', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('room', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='messages', to='room.room')),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='messages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('date_added',),
            },
        ),
    ]
