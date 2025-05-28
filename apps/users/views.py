from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserForm
from django.contrib.auth.decorators import login_required


from web_project import TemplateLayout  # Nếu bạn dùng layout này

User = get_user_model()


@login_required(login_url='/accounts/login/')

class UsersView(TemplateView):
    template_name = 'user_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('q', '').strip()
        if search_query:
            context['users'] = User.objects.filter(ten_phong_ban__icontains=search_query)
        else:
            context['users'] = User.objects.all()
        context['search_query'] = search_query
        context = TemplateLayout.init(self, context)
        return context


class UsersView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'
    login_url = '/users/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = TemplateLayout.init(self, context)
        return context

class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('user_list')
    login_url = '/accounts/login/'

    def form_valid(self, form):
        user = form.save(commit=False)
        if form.cleaned_data.get('mat_khau'):
            user.set_password(form.cleaned_data['mat_khau'])
        user.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = TemplateLayout.init(self, context)
        return context

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/user_form.html'
    success_url = reverse_lazy('user_list')
    login_url = '/accounts/login/'

    def form_valid(self, form):
        user = form.save(commit=False)
        if form.cleaned_data.get('mat_khau'):
            user.set_password(form.cleaned_data['mat_khau'])
        user.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = TemplateLayout.init(self, context)
        return context

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'users/user_confirm_delete.html'
    success_url = reverse_lazy('user_list')
    login_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = TemplateLayout.init(self, context)
        return context


# def user_login(request):
#     if request.method == 'POST':
#         ten_dang_nhap = request.POST['ten_dang_nhap']
#         password = request.POST['password']
#         user = authenticate(request, ten_dang_nhap=ten_dang_nhap, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('user_list')
#         else:
#             messages.error(request, 'Tên đăng nhập hoặc mật khẩu không đúng!')
#     return render(request, 'users/login.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('ten_dang_nhap')  # field name trên form
        password = request.POST.get('mat_khau')

        user = authenticate(request, ten_dang_nhap=username, password=password)  # CHỖ SỬA NÈ 👈
        if user is not None:
            login(request, user)
            return redirect('user_list')
        else:
            messages.error(request, 'Tên đăng nhập hoặc mật khẩu không đúng!')
            return render(request, 'users/login.html', {'username': username})

    return render(request, 'users/login.html')
