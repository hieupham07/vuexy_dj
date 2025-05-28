from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class Kho(models.Model):
    ten_kho = models.CharField(max_length=255, unique=True)
    thong_tin = models.TextField(blank=True, null=True)
    kho_cha = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='kho_con'
    )

    def __str__(self):
        return self.ten_kho

    def get_children(self):
        return self.kho_con.all()