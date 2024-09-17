from django.shortcuts import render, redirect
from base.forms import CadastroForm


def inicio(request):
    return render(request, 'inicio.html')


def cadastro(request):
    sucesso = False
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        form.save()
        sucesso = True
        return redirect('/cadastro')
    contexto = {
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'cadastro.html', contexto)
