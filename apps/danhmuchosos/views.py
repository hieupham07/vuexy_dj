from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib import messages
from .models import DanhMucHoSo
from .forms import DanhMucHoSoForm
from django.views.generic import TemplateView
from web_project import TemplateLayout
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView , DeleteView

class DanhMucHoSoListView(TemplateView):
    template_name = 'danhmuchoso_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('q', '').strip()
        if search_query:
            context['danhmuchosos'] = DanhMucHoSo.objects.filter(ten_danh_muc__icontains=search_query)
        else:
            context['danhmuchosos'] = DanhMucHoSo.objects.all()
        context['search_query'] = search_query
        context = TemplateLayout.init(self, context)
        return context

class DanhMucHoSoCreateView(CreateView):
    model = DanhMucHoSo
    form_class = DanhMucHoSoForm
    template_name = 'danhmuchoso_form.html'
    success_url = reverse_lazy('danhmuchoso_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = TemplateLayout.init(self, context)
        return context

class DanhMucHoSoUpdateView(UpdateView):
    model = DanhMucHoSo
    form_class = DanhMucHoSoForm
    template_name = 'danhmuchoso_form.html'
    success_url = reverse_lazy('danhmuchoso_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = TemplateLayout.init(self, context)
        return context

class DanhMucHoSoDeleteView(DeleteView):
    model = DanhMucHoSo
    template_name = 'danhmuchoso_confirm_delete.html'
    success_url = reverse_lazy('danhmuchoso_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = TemplateLayout.init(self, context)
        return context
