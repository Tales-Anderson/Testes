from django.db import models

class Inquilino(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField()

    def __str__(self):
        return self.nome



class Apartamento(models.Model):
    id = models.AutoField(primary_key=True)
    valor = models.DecimalField(max_digits = 10,decimal_places = 2)
    qtdQuartos = models.IntegerField
    tamM3 = models.IntegerField()
    andar = models.IntegerField()
    numero = models.IntegerField()
    residente = models.ForeignKey(Inquilino, on_delete = models.CASCADE, null=True, blank=True)
    qtdQuartos = models.IntegerField()
    qtdBanheiros = models.IntegerField()
    descricao = models.CharField(max_length=255)
    disponivel = models.BooleanField(default=True)


    def __str__(self):
        return self.descricao



