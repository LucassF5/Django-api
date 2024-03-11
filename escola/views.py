from rest_framework import viewsets
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer

# A viewset é uma forma de agrupar as views comuns em um único local
class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos"""
    queryset = Aluno.objects.all() # Recebe todos os objetos do model Aluno
    serializer_class = AlunoSerializer # Classe responsável por serializar os dados

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all() # Recebe todos os objetos do model Curso
    serializer_class = CursoSerializer # Classe responsável por serializar os dados

class MatriculasViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer