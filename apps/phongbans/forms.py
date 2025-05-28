from django import forms
from apps.phongbans.models import PhongBan
# from phongbans.models import PhongBan
class PhongBanForm(forms.ModelForm):
    class Meta:
        model = PhongBan
        fields = ['ten_phong_ban', 'thong_tin', 'phong_ban_cha']
