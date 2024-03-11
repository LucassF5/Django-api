from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer

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

class ListaMatriculasAluno(generics.ListAPIView):
# ListAPIView é uma classe que fornece uma implementação básica para a listagem de dados
    """Listando as matrículas de um aluno ou aluna"""
    def get_queryset(self):
        # Método que retorna o queryset que será utilizado
        queryset = Matricula.objects.filter(aluno_id = self.kwargs['pk']) # Filtra as matrículas pelo id do aluno
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer