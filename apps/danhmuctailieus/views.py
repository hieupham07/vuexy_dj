from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib import messages
from .models import DanhMucTaiLieu
from .forms import DanhMucTaiLieuForm
from django.views.generic import TemplateView
from web_project import TemplateLayout
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView , DeleteView

class DanhMucTaiLieuListView(TemplateView):
    template_name = 'danhmuctailieu_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('q', '').strip()
        if search_query:
            context['danhmuctailieus'] = DanhMucTaiLieu.objects.filter(ten_danh_muc__icontains=search_query)
        else:
            context['danhmuctailieus'] = DanhMucTaiLieu.objects.all()
        context['search_query'] = search_query
        context = TemplateLayout.init(self, context)
        return context

class DanhMucTaiLieuCreateView(CreateView):
    model = DanhMucTaiLieu
    form_class = DanhMucTaiLieuForm
    template_name = 'danhmuctailieu_form.html'
    success_url = reverse_lazy('danhmuctailieu_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = TemplateLayout.init(self, context)
        return context

class DanhMucTaiLieuUpdateView(UpdateView):
    model = DanhMucTaiLieu
    form_class = DanhMucTaiLieuForm
    template_name = 'danhmuctailieu_form.html'
    success_url = reverse_lazy('danhmuctailieu_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = TemplateLayout.init(self, context)
        return context

class DanhMucTaiLieuDeleteView(DeleteView):
    model = DanhMucTaiLieu
    template_name = 'danhmuctailieu_confirm_delete.html'
    success_url = reverse_lazy('danhmuctailieu_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = TemplateLayout.init(self, context)
        return context
