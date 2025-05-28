
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib import messages
from .forms import HoSoForm
from .models import HoSo
from django.views.generic import TemplateView
from web_project import TemplateLayout
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView , DeleteView

class HoSosView(TemplateView):
    template_name = 'hoso_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Lấy tham số tìm kiếm từ query string
        search_query = self.request.GET.get('q', '').strip()
        if search_query:
            # Lọc theo tên phòng ban hoặc thông tin (bạn có thể thay đổi trường search phù hợp)
            context['hosos'] = HoSo.objects.filter(ten_ho_so__icontains=search_query)
        else:
            context['hosos'] = HoSo.objects.all()
        context['search_query'] = search_query
        context = TemplateLayout.init(self, context)
        return context

class HoSoCreateView(CreateView):
    model = HoSo
    form_class = HoSoForm
    template_name = 'hoso_form.html'
    success_url = reverse_lazy('hoso_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = TemplateLayout.init(self, context)
        return context

class HoSoUpdateView(UpdateView):
    model = HoSo
    form_class = HoSoForm
    template_name = 'hoso_form.html'  # hoặc 'HoSos/hoso_update.html' nếu bạn tách riêng
    success_url = reverse_lazy('hoso_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = TemplateLayout.init(self, context)
        return context

class HoSoDeleteView(DeleteView):
    model = HoSo
    template_name = 'hoso_delete.html'
    success_url = reverse_lazy('hoso_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = TemplateLayout.init(self, context)
        return context


