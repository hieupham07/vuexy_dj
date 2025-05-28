from django import forms
from django.db import models
from apps.danhmuchosos.models import DanhMucHoSo
# from phongbans.models import PhongBan
class DanhMucHoSoForm(forms.ModelForm):
   
    class Meta:
        model = DanhMucHoSo
        fields = ['id','ten_danh_muc', 'noi_dung','mo_ta', 'danh_muc_cha']