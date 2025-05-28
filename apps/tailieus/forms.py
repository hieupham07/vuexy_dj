from django import forms
from django.db import models
from apps.tailieus.models import TaiLieu
# from phongbans.models import PhongBan
class TaiLieuForm(forms.ModelForm):
   
    class Meta:
        model = TaiLieu
        fields = ['id','ma_tai_lieu','ngay_tai_lieu','ten_tai_lieu', 'noi_dung','mo_ta','ngay_ky','nguoi_ky','file_tai_lieu', 'danh_muc']