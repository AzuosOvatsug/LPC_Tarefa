from django.db import models
from django.utils import timezone


class Usuario(models.Model):
    nome = models.CharField('nome', max_length=100)
    email = models.EmailField('Email')
    senha = models.PasswordField('senha')

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()

        super(Usuario, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.nome)


class Projeto(models.Model):
    nome = models.CharField('nome', max_length=70)

    def __str__(self):
        return '{}'.format(self.nome)


class Tarefa(Projeto):
    nome = models.CharField('nome', max_length=200)
    dataEHoraDeInicio = models.DateTimeField()
    usuario = models.ForeignKey('Usuario')
    projeto = models.ForeignKey('Projeto')

    def __str__(self):
        return '{}'.format(self.nome)

class ProjetoUsuario(Usuario, Projeto):
    usuario = models.ForeignKey('Usuario')
    projeto = models.ForeignKey('Projeto')

    def __str__(self):
        return '{}'.format(self.usuario)
