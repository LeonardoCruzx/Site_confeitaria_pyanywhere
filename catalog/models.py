from django.db import models


# Create your models here.
class ModelCategoria(models.Model):
    tipo = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )
    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        

class ModelQuantidadeFatias(models.Model):
    quantidade_de_fatias = models.PositiveIntegerField()

    def __str__(self):
        return str(self.quantidade_de_fatias)

    class Meta:
        verbose_name = 'quantidade de fatias'
        verbose_name_plural = 'quantidade de fatias'

class ModelDoces(models.Model):
    nome = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )
    quantidade_de_fatias = models.ForeignKey(
        'ModelQuantidadeFatias',
        on_delete=models.CASCADE,
        null=True,
        blank=False
    )
    categoria = models.ForeignKey(
        'ModelCategoria',
        on_delete=models.CASCADE,
        null=True,
        blank=False
    )
    preco = models.PositiveIntegerField(
        null=True,
        blank=False
    )
    descricao = models.TextField(
        max_length=200,
        null=True,
        blank=False
    )
    imagem = models.ImageField(
        upload_to='imagens_de_doces',
        null=True,
        blank=False
    )

    # __str__ muda o nome do objeto na lista de bolos do admin
    def __str__(self):
        return self.nome
    # o verbose_name_plural muda o nome do modelo no django admin
    class Meta:
        verbose_name = 'doce'
        verbose_name_plural = 'doces'



