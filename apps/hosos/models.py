from django.db import models
from apps.danhmuchosos.models import DanhMucHoSo
from django.contrib.auth.models import AbstractUser, BaseUserManager


class HoSo(models.Model):
    id = models.AutoField(primary_key=True)
    ma_ho_so = models.CharField(max_length=250, blank=True, null=True)
    ngay_ho_so = models.DateField(blank=True, null=True)
    ten_ho_so = models.CharField(max_length=250)
    noi_dung = models.TextField(blank=True, null=True)
    mo_ta = models.TextField(blank=True, null=True)
    ngay_ky = models.DateField(blank=True, null=True)
    nguoi_ky = models.CharField(max_length=250, blank=True, null=True)
    file_ho_so = models.FileField(upload_to='pdfs/', blank=True, null=True)
    danh_muc = models.ForeignKey(DanhMucHoSo, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.ten_ho_so

