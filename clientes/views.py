from rest_framework import viewsets, filters
from clientes.models import Cliente
from clientes.serializer import ClienteSerializer
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated


class ClientesViewSet(viewsets.ModelViewSet):
    """Listando todos os clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend,
                       filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']                      # Ordenação da API
    search_fields = ['nome', 'cpf', ]               # Filtro de busca
    filterset_fields = ['ativo']                    # Filtro de campo
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
