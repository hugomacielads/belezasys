from django.db import models

LISTA_SEXO = (
    ("M", "Masculino"),
    ("F", "Feminino")
)


# Create your views here.
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    telefone = models.TextField(max_length=11)
    email = models.CharField(max_length=100)
    data_nasc = models.DateTimeField()
    endereco = models.DateTimeField(max_length=200)
    sexo = models.CharField(max_length=9, choices=LISTA_SEXO)

    def __str__(self):
        return self.nome