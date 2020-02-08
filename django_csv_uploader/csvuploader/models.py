from django.db import models

class User(models.Model):
    codice_cliente = models.IntegerField()
    codice_fiscale = models.CharField(max_length=50)
    ragione_sociale = models.TextField()
    nome = models.CharField(max_length=50)
    indirizzo = models.CharField(max_length=50)
    cap = models.IntegerField()
    comune = models.TextField()
    provincia = models.TextField()
    codice_stato = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.nome}'
    
