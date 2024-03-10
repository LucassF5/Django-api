from rest_framework import serializers
from escola.models import Aluno, Curso

# O Serializer vai servir como um filtro de dados 
# a serem Disponibilizados para a API

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:  # Classe que define o modelo que será serializado
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__' # Indica que vai utilizar todos os campos do model
