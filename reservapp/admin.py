from django.contrib import admin
from reservapp.models import Usuario, Restaurante, Reserva, RestauranteFavorito, ItemCardapio

admin.site.register(Usuario)
admin.site.register(Restaurante)
admin.site.register(Reserva)
admin.site.register(RestauranteFavorito)
admin.site.register(ItemCardapio)