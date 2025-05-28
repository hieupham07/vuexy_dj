from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib import messages
from .forms import PhongBanForm
from .models import PhongBan
from django.views.generic import TemplateView
from web_project import TemplateLayout
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView , DeleteView

class PhongbansView(TemplateView):
    template_name = 'phongban_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Lấy tham số tìm kiếm từ query string
        search_query = self.request.GET.get('q', '').strip()
        if search_query:
            # Lọc theo tên phòng ban hoặc thông tin (bạn có thể thay đổi trường search phù hợp)
            context['phongbans'] = PhongBan.objects.filter(ten_phong_ban__icontains=search_query)
        else:
            context['phongbans'] = PhongBan.objects.all()
        context['search_query'] = search_query
        context = TemplateLayout.init(self, context)
        return context

class PhongbanCreateView(CreateView):
    model = PhongBan
    form_class = PhongBanForm
    template_name = 'phongban_form.html'
    success_url = reverse_lazy('phongban_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = TemplateLayout.init(self, context)
        return context

class PhongbanUpdateView(UpdateView):
    model = PhongBan
    form_class = PhongBanForm
    template_name = 'phongban_form.html'  # hoặc 'phongbans/phongban_update.html' nếu bạn tách riêng
    success_url = reverse_lazy('phongban_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = TemplateLayout.init(self, context)
        return context

class PhongbanDeleteView(DeleteView):
    model = PhongBan
    template_name = 'phongban_confirm_delete.html'
    success_url = reverse_lazy('phongban_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = TemplateLayout.init(self, context)
        return context

