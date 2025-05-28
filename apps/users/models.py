from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager
from apps.phongbans.models import PhongBan




class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, ten_dang_nhap, email=None, password=None, **extra_fields):
        if not ten_dang_nhap:
            raise ValueError('The Tên đăng nhập must be set')
        email = self.normalize_email(email)
        user = self.model(ten_dang_nhap=ten_dang_nhap, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, ten_dang_nhap, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(ten_dang_nhap, email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None  # Loại bỏ username mặc định
    ten_dang_nhap = models.CharField(max_length=150, unique=True, verbose_name="Tên đăng nhập")
    thong_tin = models.TextField(blank=True, null=True)
    ngay_sinh = models.DateField(blank=True, null=True)
    gioi_tinh = models.CharField(
        max_length=10,
        choices=[('Nam', 'Nam'), ('Nữ', 'Nữ'), ('Khác', 'Khác')],
        blank=True,
        null=True
    )
    hinh_anh = models.ImageField(upload_to='user_images/', blank=True, null=True)
    trinh_do = models.CharField(max_length=100, blank=True, null=True)
    phong_ban = models.ForeignKey(
        PhongBan,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='users'
    )

    USERNAME_FIELD = 'ten_dang_nhap'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.ten_dang_nhap