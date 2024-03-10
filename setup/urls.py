from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet
from rest_framework import routers

# ROUTER é uma forma de agrupar as views comuns em um único local
router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
# router.register('path', ViewSet, basename='Nome')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ), # Inclui as rotas do router
]
