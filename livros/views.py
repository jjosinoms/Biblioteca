from django.shortcuts import render, get_object_or_404
from .models import Autor, Editora, Livro
from .forms import CadastroLivro
from django.shortcuts import redirect

# Create your views here.
def home(request):
	livro = Livro.objects.filter()
	#livro = Livro.objects.order_by('id')
	return render(request, 'index.html', {"livro":livro})

def cadastro(request):

	if request.method == "POST":
		formulario = CadastroLivro(request.POST)
		if formulario.is_valid():
			livro = formulario.save(commit=False)
			livro.save()
			return redirect('/index.html')
	else:
		formulario = CadastroLivro()
	return render(request, 'cadastro-livro.html', {"formulario":CadastroLivro()})

def busca(request):
	nome_original = request.POST.get('busca') 
	nome = nome_original
	busca = Livro.objects.filter(slug=nome) or Livro.objects.filter(nome=nome)
	return render(request, 'busca.html', {"busca":busca})

def detalhe(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, 'detalhe.html', {'livro': livro})
