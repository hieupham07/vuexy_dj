from django import forms
from django.db import models
from apps.danhmuctailieus.models import DanhMucTaiLieu
# from phongbans.models import PhongBan
class DanhMucTaiLieuForm(forms.ModelForm):
   
    class Meta:
        model = DanhMucTaiLieu
        fields = ['id','ten_danh_muc','mo_ta', 'danh_muc_cha']