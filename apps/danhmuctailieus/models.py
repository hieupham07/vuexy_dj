from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class DanhMucTaiLieu(models.Model):
    id = models.AutoField(primary_key=True)
    ten_danh_muc = models.CharField(max_length=250)
    mo_ta = models.TextField(blank=True, null=True)
    danh_muc_cha = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='danh_muc_con'
    )

    def __str__(self):
        return self.ten_danh_muc

    def get_children(self):
        return self.danh_muc_con.all()