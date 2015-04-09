from django.db import models
from django.contrib.auth.models import User  

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sendedMessages', verbose_name='de')
    recipient = models.ForeignKey(User, related_name='inboxMessages', verbose_name='para')
    content = models.CharField(max_length=100, verbose_name='mensaje')

    class Meta:
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'
