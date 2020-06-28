from django.db import models

# Create your models here.
class Codigo(models.Model):
    id = models.AutoField(primary_key = True)
    codigo = models.IntegerField()
    reajustable = models.BooleanField()

    def __str__(self):
        return self.reajustable

class Dia(models.Model):
    id = models.AutoField(primary_key=True)
    dias = models.IntegerField()
    condicion = models.TextField()
    codigo_id = models.ForeignKey(Codigo, on_delete=models.CASCADE)

    def __str__(self):
        return self.condicion

class Uf(models.Model):
    id = models.AutoField(primary_key=True)
    uf = models.IntegerField()
    condicion = models.TextField()
    codigo_id = models.ForeignKey(Codigo, on_delete=models.CASCADE)

    def __str__(self):
        return self.condicion
