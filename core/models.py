from django.db import models


class GrupoProduto(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    marca = models.ForeignKey(GrupoProduto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
