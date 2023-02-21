from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Room(models.Model):
    name = models.CharField(
        verbose_name='Название комнаты',
        help_text='Поле для имени комнаты',
        max_length=50,
        blank=False
    )
    slug = models.SlugField(unique=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta():
        ordering = ('-create_date',)
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

    def get_absolute_url(self):
        return reverse('rooms:room_detail', kwargs={'room_slug': self.slug})

    def __str__(self):
        return self.name[:15]


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages',
                             on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages',
                             on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)
