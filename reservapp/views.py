from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from reservapp.models import Usuario, Restaurante, Reserva, RestauranteFavorito, ItemCardapio
from reservapp.serializer import UsuarioSerializer, RestauranteSerializer, ReservaSerializer,RestauranteFavoritoSerializer, ItemCardapioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    """Exibindo todas os usuarios"""
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nome']
    filter_backends[1].search_param = 'q'

class RestauranteViewSet(viewsets.ModelViewSet):
    """Exibindo todos os restaurantes"""
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['categoria']
    filter_backends[1].search_param = 'q'

class ReservaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as reservas"""
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['usuario_id__id']
    filter_backends[1].search_param = 'q'

class RestauranteFavoritoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os restaurantes favoritos"""
    queryset = RestauranteFavorito.objects.all()
    serializer_class = RestauranteFavoritoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['usuario_id__id']
    filter_backends[1].search_param = 'q'

class ItemCardapioViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cardapios"""
    queryset = ItemCardapio.objects.all()
    serializer_class = ItemCardapioSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['restaurante_id__id']
    filter_backends[1].search_param = 'q'
