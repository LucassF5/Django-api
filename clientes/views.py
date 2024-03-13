from rest_framework import viewsets, generics
from clientes.models import Cliente
from clientes.serializer import ClienteSerializer
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

class ClientesViewSet(viewsets.ModelViewSet):
    """Listando todos os clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]