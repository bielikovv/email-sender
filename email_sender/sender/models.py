from django.db import models

class SendMail(models.Model):
    theme = models.CharField(max_length=200, verbose_name='theme')
    content = models.TextField(verbose_name='content')
    name = models.EmailField(verbose_name='mail', null=True)
