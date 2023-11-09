from django.db import models


class Marca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Modelo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False)
    cpf = models.CharField(max_length=20, null=False, blank=False)
    nascimento = models.DateField(null=False, blank=False)
    celular1 = models.CharField(max_length=20, null=True, blank=True)
    celular2 = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ano_modelo = models.CharField(max_length=4, null=True, blank=True)
    ano_fabricacao = models.CharField(max_length=4, null=True, blank=True)
    placa = models.CharField(max_length=20, null=False, blank=False)
    cor = models.CharField(max_length=20, null=False, blank=False)
    chassis = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.placa
