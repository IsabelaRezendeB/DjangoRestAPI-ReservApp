from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from reservapp.views import ListaItemPorTipo, ListaTiposItem, RestauranteNomeAPIView, UsuarioViewSet, ReservaViewSet, RestauranteFavoritoViewSet, ItemCardapioViewSet, RestauranteViewSet
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="ReservApp",
      default_version='v1',
      description="Reserva de Restaurantes",
      terms_of_service="#",
      contact=openapi.Contact(email="exemplo@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

router = routers.DefaultRouter()
router.register('usuarios', UsuarioViewSet, basename = 'Usuarios')
router.register('restaurantes', RestauranteViewSet, basename = 'Restaurantes')
router.register('reserva', ReservaViewSet, basename = 'Reservas')
router.register('restaurantefavorito', RestauranteFavoritoViewSet, basename = 'Restaurantes Favoritos')
router.register('itemcardapio', ItemCardapioViewSet, basename = 'Items dos Cardapios')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('itens/<int:restaurante_id>/<str:tipoItem>/', ListaItemPorTipo.as_view()),
    path('itensrestaurante/<int:restaurante_id>/itens/', ListaTiposItem.as_view(), name='lista-item-por-tipo'),
    path('restaurante/<str:nome>/', RestauranteNomeAPIView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]