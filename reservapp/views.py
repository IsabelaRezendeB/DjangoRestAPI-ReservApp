from rest_framework import viewsets, filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from reservapp.models import Usuario, Restaurante, Reserva, RestauranteFavorito, ItemCardapio
from reservapp.serializer import UsuarioSerializer, RestauranteSerializer, ReservaSerializer,RestauranteFavoritoSerializer, ItemCardapioSerializer
from rest_framework.response import Response

class UsuarioViewSet(viewsets.ModelViewSet):
    """Exibindo todas os usuarios"""
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['email']
    filter_backends[1].search_param = 'q'

class RestauranteViewSet(viewsets.ModelViewSet):
    """Exibindo todos os restaurantes"""
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['categoria']
    filter_backends[1].search_param = 'q'

class RestauranteNomeAPIView(generics.ListAPIView):
    """Exibindo restaurantes filtrados por nome"""
    def get_queryset(self):
        nome = self.kwargs['nome']
        queryset = Restaurante.objects.filter(nome=nome)
        return queryset

    serializer_class = RestauranteSerializer

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
    """Exibindo todos os itens dos cardapios"""
    queryset = ItemCardapio.objects.all()
    serializer_class = ItemCardapioSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['restaurante_id__id']
    filter_backends[1].search_param = 'q'

class ListaItemPorTipo(generics.ListAPIView):
    """Listando itens por tipo"""

    def get_queryset(self):

        queryset = ItemCardapio.objects.filter(restaurante_id=self.kwargs['restaurante_id'], tipoItem=self.kwargs['tipoItem'])
        return queryset

    serializer_class = ItemCardapioSerializer

class ListaTiposItem(generics.ListAPIView):
    """Listando os tipos de item"""
    serializer_class = ItemCardapioSerializer

    def get(self, request, restaurante_id):
        tipo_items = ItemCardapio.objects.filter(restaurante_id=restaurante_id).values_list('tipoItem', flat=True).distinct()
        return Response(tipo_items)