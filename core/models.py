from django.db import models


UNIDADE_CHOICES = (
        ("UN", "Unidade"),
        ("MT", "Metro linear"),
        ("M2", "Metro quadrado"),
        ("M3", "Metro cubico"),
        ("L", "Litro"),
        ("KG", "Quilograma")
)


class GrupoProduto(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    grupo = models.ForeignKey(GrupoProduto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=150, blank=False, null=False)
    unidade = models.CharField(max_length=2, choices=UNIDADE_CHOICES, blank=False, null=False)

    def __str__(self):
        return self.nome


class Especialidade(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.nome


class Profissional(models.Model):
    nome = models.CharField(max_length=150, null=False, blank=False)
    cpf = models.CharField(max_length=20, null=False, blank=False)
    celular1 = models.CharField(max_length=20, null=True, blank=True)
    celular2 = models.CharField(max_length=20, null=True, blank=True)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)

