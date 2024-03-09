from django.contrib import admin
from escola.models import Aluno, Curso

class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome') # Nome dos elementos que vão poder ser selecionáveis
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Aluno, Alunos)
# admin.site.register(nome_da_classe, nome_da_classe_admin)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao', 'nivel')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso', 'nivel')

admin.site.register(Curso, Cursos)