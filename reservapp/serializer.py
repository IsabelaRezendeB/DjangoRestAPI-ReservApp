from rest_framework import serializers
from reservapp.models import Usuario, Restaurante, Reserva, RestauranteFavorito, ItemCardapio

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

class RestauranteFavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestauranteFavorito
        fields = '__all__'

class ItemCardapioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCardapio
        fields = '__all__'
