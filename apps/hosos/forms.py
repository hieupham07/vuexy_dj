from django import forms
from django.db import models
from apps.hosos.models import HoSo
# from phongbans.models import PhongBan
class HoSoForm(forms.ModelForm):
    class Meta:
        model = HoSo
        fields = ['id','ma_ho_so','ngay_ho_so','ten_ho_so', 'noi_dung','mo_ta','ngay_ky','nguoi_ky','file_ho_so', 'danh_muc']