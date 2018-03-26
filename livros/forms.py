from django import forms

from .models import Livro

class CadastroLivro(forms.ModelForm):
	file = forms.FileField(
    label='Select a file',
    help_text='max. 42 megabytes'
    )

	class Meta:
		model = Livro
		fields = ('nome','slug','autor','editora','sinopse','imagem','file',)
		