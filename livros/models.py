from django.db import models
from django.contrib import admin
from django.template.defaultfilters import slugify



# Create your models here.
class Autor(models.Model):

	nome = models.CharField(max_length=45)
	sobrenome = models.CharField(max_length=45)

	def __str__(self):
		return self.nome

class Editora(models.Model):

	nome = models.CharField(max_length=45)

	def __str__(self):
		return self.nome

class Livro(models.Model):
	nome = models.CharField(max_length=45)
	slug = models.SlugField('Atalho')
	autor = models.ForeignKey(Autor)
	editora = models.ForeignKey(Editora)
	sinopse = models.TextField(max_length=300)
	imagem = models.ImageField(upload_to = "media",blank=True)
	def __str__(self):
		return self.nome

class Usuario(models.Model):
	nome = models.CharField(max_length=45)
	sobrenome = models.CharField(max_length=45)
	email = models.CharField('email', max_length=100)
	senha = models.CharField('senha', max_length=40)

	def __str__(self):
		return self.email