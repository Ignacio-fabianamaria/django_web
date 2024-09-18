from django.shortcuts import render, redirect
from cursos.forms import CursoForm


def criar_curso(request):
    form = CursoForm(request.POST or None)
    sucesso = False
    if form.is_valid():
        sucesso = True
        return redirect('/curso/criar_curso')
    contexto = {
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'criar_curso.html', contexto)
