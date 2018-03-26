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
	sinopse = models.TextField(max_length=500)
	imagem = models.ImageField(upload_to = "media",blank=True)
	file  = models.FileField(upload_to = "media/")
	def __str__(self):
		return self.nome
