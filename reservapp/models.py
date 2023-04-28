from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    senha = models.CharField(max_length = 100)
    fotoURL = models.CharField(max_length = 300)

    def __str__(self):
        return self.nome

class Restaurante(models.Model):
    nome = models.CharField(max_length = 100)
    endereco = models.CharField(max_length = 100)
    horariosFuncionamento = models.CharField(max_length = 100)
    avaliacao = models.IntegerField(default= 0)
    descricao = models.CharField(max_length = 100)
    imagemFundoURL = models.CharField(max_length = 300)
    iconeURL = models.CharField(max_length = 300)
    CATEGORIA = (
        ('P', 'Pizzaria'),
        ('H', 'Hamburgueria'),
        ('J', 'Japa'),
        ('C', 'Comidas Tradicionais'),
        ('D', 'Doceria'),
        ('I', 'Italiano'),
        ('O', 'Outras')
    )
    categoria = models.CharField(max_length = 1, choices = CATEGORIA, default = 'O')

    def __str__(self):
        return self.nome

class Reserva(models.Model):
    data = models.DateField()
    horario = models.TimeField()
    numeroPessoas = models.IntegerField()
    usuario_id = models.ForeignKey(Usuario, on_delete= models.PROTECT, related_name="reservas")
    restaurante_id = models.ForeignKey(Restaurante, on_delete= models.PROTECT, related_name="reservas")

    def __str__(self):
        return "%s - %s" %(self.usuario_id, self.restaurante_id)

class RestauranteFavorito(models.Model):
    usuario_id = models.ForeignKey(Usuario, on_delete= models.PROTECT, related_name="restaurantefavorito")
    restaurante_id = models.ForeignKey(Restaurante, on_delete= models.PROTECT, related_name="restaurantefavorito")

    def __str__(self):
        return "%s - %s" %(self.usuario_id, self.restaurante_id)

class ItemCardapio(models.Model):
    nome = models.CharField(max_length = 100)
    preco = models.FloatField()
    tipoItem = models.CharField(max_length = 100)
    descricao = models.CharField(max_length = 100)
    restaurante_id = models.ForeignKey(Restaurante, on_delete= models.PROTECT, related_name="itemcardapio")

    def __str__(self):
        return self.nome