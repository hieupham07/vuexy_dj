from django import forms
from django.contrib.auth import get_user_model
from apps.phongbans.models import PhongBan

User = get_user_model()

class UserForm(forms.ModelForm):
    phong_ban = forms.ModelChoiceField(
        queryset=PhongBan.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    mat_khau = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
        required=False
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'autocomplete': 'username'})
    )
    ngay_sinh = forms.DateField(
        required=False,
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'text', 'placeholder': 'dd/mm/yyyy'}),
        input_formats=['%d/%m/%Y', '%Y-%m-%d']
    )

    class Meta:
        model = User
        fields = [
            'ten_dang_nhap', 'email', 'thong_tin', 'ngay_sinh',
            'gioi_tinh', 'mat_khau', 'hinh_anh', 'trinh_do', 'phong_ban'
        ]