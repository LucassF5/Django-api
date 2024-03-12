from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

# O Serializer vai servir como um filtro de dados
# a serem Disponibilizados para a API


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:  # Classe que define o modelo que será serializado
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'  # Indica que vai utilizar todos os campos do model


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []  # Outra forma de mostrar todos os campos do model
        # Indica que não vai excluir nenhum campo do model

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    # Mostra no nome do campo a descrição do curso
    periodo = serializers.SerializerMethodField()
    # Mostra o nome do campo periodo
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()
        # Retorna o valor do campo periodo em formato de texto
    
class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno = serializers.ReadOnlyField(source = 'aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno']