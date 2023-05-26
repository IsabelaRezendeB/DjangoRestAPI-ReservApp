from django.test import TestCase
from reservapp.models import Usuario, Restaurante, Reserva, RestauranteFavorito, ItemCardapio

import xmlrunner
from django.test.runner import DiscoverRunner


class XMLTestRunner(DiscoverRunner):
    def run_suite(self, suite, **kwargs):
        runner = xmlrunner.XMLTestRunner(output='test-reports')
        return runner.run(suite)


class UsuarioModelTestCase(TestCase):

    def setUp(self):
        self.usuario = Usuario(
            nome = 'Isabela',
            email = 'isabela@gmail.com',
            senha = 'senha',
            fotoURL = 'www.foto.com'
        )
    
    def test_verifica_atributos(self):
        """Verifica Atributos do model Usuario"""
        self.assertEqual(self.usuario.nome, 'Isabela')
        self.assertEqual(self.usuario.email, 'isabela@gmail.com')
        self.assertEqual(self.usuario.senha, 'senha')
        self.assertEqual(self.usuario.fotoURL, 'www.foto.com')

class RestauranteModelTestCase(TestCase):

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
    
    def test_verifica_atributos(self):
        """Verifica Atributos do model Restaurante"""
        self.assertEqual(self.restaurante.nome, 'Iwata')
        self.assertEqual(self.restaurante.endereco, 'Rua Bairro Cidade')
        self.assertEqual(self.restaurante.horariosFuncionamento, '17:00-23:00')
        self.assertEqual(self.restaurante.avaliacao, 3)
        self.assertEqual(self.restaurante.descricao, 'Comida Japonesa')
        self.assertEqual(self.restaurante.imagemFundoURL, 'www.foto.com')
        self.assertEqual(self.restaurante.iconeURL, 'www.foto.com')
        self.assertEqual(self.restaurante.categoria, 'J')
        
class ReservaModelTestCase(TestCase):

    def setUp(self):
        self.reserva = Reserva(
            data = '31/05/2023',
            horario = '19:00',
            numeroPessoas = 2,
        )
    
    def test_verifica_atributos(self):
        """Verifica Atributos do model Reserva"""
        self.assertEqual(self.reserva.data, '31/05/2023')
        self.assertEqual(self.reserva.horario, '19:00')
        self.assertEqual(self.reserva.numeroPessoas, 2)

class ItemCardapioModelTestCase(TestCase):

    def setUp(self):
        self.item = ItemCardapio(
            nome = 'Guarana',
            preco = 7.80,
            tipoItem = 'Bebida',
            descricao = 'Guarana de 1L'
        )
    
    def test_verifica_atributos(self):
        """Verifica Atributos do model Item Cardapio"""
        self.assertEqual(self.item.nome, 'Guarana')
        self.assertEqual(self.item.preco, 7.80)
        self.assertEqual(self.item.tipoItem, 'Bebida')
        self.assertEqual(self.item.descricao, 'Guarana de 1L')