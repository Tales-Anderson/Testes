from django.test import TestCase

from main.models import *
from django.urls import reverse

# Create your tests here.

# Test no model Model
class NewsTestCase(TestCase):

    def setUp(self):
        Apartamento.objects.create(
            id = 1,
            valor = 2000.00,
            qtdQuartos = 2,
            tamM3 = 50,
            andar =3,
            numero = 303,
            qtdBanheiros = 2,
            descricao = "Apartamento 303",
            disponivel = True,
        )
  
        Inquilino.objects.create(
            id=1,
            nome="Tales",
            cpf= 11111111111
        )
            
#testa se o Inquilino existe
    #def test_inquilino(self):
    #    inquilino = Inquilino.objects.get(id=1)
    #    self.assertEquals(inquilino.id, 1)

#testa se o Cpf está correto
    #def test_inquilinoCpf(self):
    #    inquilino = Inquilino.objects.get(id=1)
    #    self.assertEquals(inquilino.cpf, 11111111111)

#testa se o valor do aluguel está correto
    #def test_valorAluguel(self):
    #    apartamento = Apartamento.objects.get(id=1)
    #    self.assertEquals(apartamento.valor, 2000.00)


#teste  para saber se o apartamento está realmente disponivel
    #def test_apartamentoDisponivel(self):
    #    apartamento = Apartamento.objects.get(id=1)
    #    self.assertEquals(apartamento.disponivel, True)


#teste  para saber se a quantidade de quartos está correta
    #def test_qtdQuartos(self):
    #    apartamento = Apartamento.objects.get(id=1)
    #    self.assertEquals(apartamento.qtdQuartos, 2)

#teste  para saber se a quantidade de Metros quadrados está correto 
    #def test_metrosQuadrados(self):
    #    apartamento = Apartamento.objects.get(id=1)
    #    self.assertEquals(apartamento.tamM3, 50)
    
    
#teste  para saber se o numero do andar
    #def test_andar(self):
    #    apartamento = Apartamento.objects.get(id=1)
    #    self.assertEquals(apartamento.andar, 3)

#teste  para saber se o numero do apartamento esta correto
    #def test_numeroAndar(self):
    #    apartamento = Apartamento.objects.get(id=1)
    #    self.assertEquals(apartamento.numero, 303)


# # Teste em View
#class NewsViewTestCase(TestCase):

# Teste se a View Home está funcionando 
    #def test_home_status_200(self):
    #    response = self.client.get(reverse('url_home'))
    #    self.assertEquals(response.status_code, 200)

#Teste se a View HomeFunc está funcionando 
    #def test_home_status_200(self):
    #    response = self.client.get(reverse('url_HomeFunc'))
    #    self.assertEquals(response.status_code, 200)



