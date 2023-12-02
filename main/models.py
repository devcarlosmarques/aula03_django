from django.db import models
from django.contrib.auth import get_user_model

class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(null=True, blank=True,max_length=15)
    email = models.EmailField()
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.nome