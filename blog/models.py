#models.Model - significa que a class e um modelo de Django, então o Django sabe que ele deve ser #salvo no banco de dados
# author = models.Foreignkey('auth.User')#este é um link para outro modelo
# title = models.CharField(max_length=200)#assim que você define um texto com um numero limitado de caracteres
# text = models.TextField()#esse é para textos longos, sem limite.
# created_date = models.DateTimeField(default=timezone.now)#data e hora
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
