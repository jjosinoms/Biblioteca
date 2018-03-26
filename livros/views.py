from django.shortcuts import render, get_object_or_404
from .models import Autor, Editora, Livro
from .forms import CadastroLivro
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


# Create your views here.
def home(request):
	livro = Livro.objects.filter()
	#livro = Livro.objects.order_by('id')
	return render(request, 'index.html', {"livro":livro})

def cadastro(request):
    if request.method == 'POST':
    	form = CadastroLivro(request.POST, request.FILES)
    	if form.is_valid():
            form.save()
            return redirect('home')
    else:
    	form = CadastroLivro()
    return render(request, 'cadastro-livro.html', {"form":form})

def busca(request):
	nome_original = request.POST.get('busca') 
	nome = nome_original
	busca = Livro.objects.filter(slug=nome) or Livro.objects.filter(nome=nome) 
	return render(request, 'busca.html', {"busca":busca})

def detalhe(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, 'detalhe.html', {'livro': livro})


