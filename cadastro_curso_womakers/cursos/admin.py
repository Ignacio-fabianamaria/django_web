from django.contrib import admin
from cursos.models import Curso


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'nivel', 'descricao', 'data_do_curso']
    search_fields = ['titulo', 'nivel']
    list_filter = ['data_do_curso']