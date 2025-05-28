from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class PhongBan(models.Model):
    ten_phong_ban = models.CharField(max_length=255, unique=True)
    thong_tin = models.TextField(blank=True, null=True)
    phong_ban_cha = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='phong_ban_con'
    )

    def __str__(self):
        return self.ten_phong_ban

    def get_children(self):
        return self.phong_ban_con.all()