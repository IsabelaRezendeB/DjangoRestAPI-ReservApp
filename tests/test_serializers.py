from django.test import TestCase
from reservapp.models import Usuario, Restaurante, Reserva, ItemCardapio
from reservapp.serializer import UsuarioSerializer, RestauranteSerializer, ReservaSerializer, ItemCardapioSerializer

class UsuarioSerializerTestCase(TestCase):

    def setUp(self):
        self.usuario = Usuario(
            nome = 'Isabela',
            email = 'isabela@gmail.com',
            senha = 'senha',
            fotoURL = 'www.foto.com'
        )
        self.serializer = UsuarioSerializer(instance = self.usuario)
    
    def test_verifica_campos(self):
        """Verifica se os campos de Usuario estão sendo serializados corretamente"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'nome', 'email', 'senha', 'fotoURL']))
    
    def test_verifica_conteudo(self):
        """Verifica se o conteúdo de Usuario está sendo serializado corretamente"""
        data = self.serializer.data
        self.assertEqual(data['nome'], self.usuario.nome)
        self.assertEqual(data['email'], self.usuario.email)
        self.assertEqual(data['senha'], self.usuario.senha)
        self.assertEqual(data['fotoURL'], self.usuario.fotoURL)

class RestauranteSerializerTestCase(TestCase):

    def setUp(self):
        self.restaurante = Restaurante(
            nome = 'Iwata',
            endereco = 'Rua Bairro Cidade',
            horariosFuncionamento = '17:00-23:00',
            avaliacao = 3,
            descricao = 'Comida Japonesa',
            imagemFundoURL = 'www.foto.com',
            iconeURL = 'www.foto.com',
            categoria = 'J'
        )
        self.serializer = RestauranteSerializer(instance = self.restaurante)
    
    def test_verifica_campos(self):
        """Verifica se os campos de Restaurante estão sendo serializados corretamente"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'nome', 'endereco', 'horariosFuncionamento', 'avaliacao', 'descricao', 'imagemFundoURL', 'iconeURL', 'categoria']))
    
    def test_verifica_conteudo(self):
        """Verifica se o conteúdo de Usuario está sendo serializado corretamente"""
        data = self.serializer.data
        self.assertEqual(data['nome'], self.restaurante.nome)
        self.assertEqual(data['endereco'], self.restaurante.endereco)
        self.assertEqual(data['horariosFuncionamento'], self.restaurante.horariosFuncionamento)
        self.assertEqual(data['avaliacao'], self.restaurante.avaliacao)
        self.assertEqual(data['descricao'], self.restaurante.descricao)
        self.assertEqual(data['imagemFundoURL'], self.restaurante.imagemFundoURL)
        self.assertEqual(data['iconeURL'], self.restaurante.iconeURL)
        self.assertEqual(data['categoria'], self.restaurante.categoria)

class ReservaSerializerTestCase(TestCase):

    def setUp(self):
        self.reserva = Reserva(
            data = '31/05/2023',
            horario = '19:00',
            numeroPessoas = 2,
        )
        self.serializer = ReservaSerializer(instance = self.reserva)
    
    def test_verifica_campos(self):
        """Verifica se os campos de Reserva estão sendo serializados corretamente"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'data', 'horario', 'numeroPessoas', 'usuario_id', 'restaurante_id']))
    
    def test_verifica_conteudo(self):
        """Verifica se o conteúdo de Reserva está sendo serializado corretamente"""
        data = self.serializer.data
        self.assertEqual(data['data'], self.reserva.data)
        self.assertEqual(data['horario'], self.reserva.horario)
        self.assertEqual(data['numeroPessoas'], self.reserva.numeroPessoas)

class ItemCardapioSerializerTestCase(TestCase):

    def setUp(self):
        self.item = ItemCardapio(
            nome = 'Guarana',
            preco = 7.80,
            tipoItem = 'Bebida',
            descricao = 'Guarana de 1L'
        )
        self.serializer = ItemCardapioSerializer(instance = self.item)
    
    def test_verifica_campos(self):
        """Verifica se os campos de ItemCardapio estão sendo serializados corretamente"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'nome', 'preco', 'tipoItem', 'descricao', 'restaurante_id']))
    
    def test_verifica_conteudo(self):
        """Verifica se o conteúdo de ItemCardapio está sendo serializado corretamente"""
        data = self.serializer.data
        self.assertEqual(data['nome'], self.item.nome)
        self.assertEqual(data['preco'], self.item.preco)
        self.assertEqual(data['tipoItem'], self.item.tipoItem)
        self.assertEqual(data['descricao'], self.item.descricao)
        