from django import forms

from .models import Livro, Usuario

class CadastroLivro(forms.ModelForm):

	class Meta:
		model = Livro
		fields = ('nome','slug','autor','editora','sinopse','imagem','file',)
		
