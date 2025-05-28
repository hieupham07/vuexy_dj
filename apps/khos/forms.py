from django import forms
from khos.models import Kho
# from phongbans.models import PhongBan
class PhongBanForm(forms.ModelForm):
    class Meta:
        model = Kho
        fields = ['ten_kho', 'thong_tin', 'kho_cha']