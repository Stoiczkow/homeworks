from django.contrib import messages
from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from products.forms import RegisterForm
from products.models import Product

User = get_user_model()


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(
            self.request,
            f"Konto dla {self.object.username} zostało utworzone. Witaj!",
        )
        return response


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'


class AllProductsView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product
    template_name = 'products/all_products.html'
    context_object_name = 'products'
    permission_required = 'products.view_product'
    raise_exception = True


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        return self.request.user.is_staff


class UsersListView(StaffRequiredMixin, ListView):
    model = User
    template_name = 'users/users_list.html'
    context_object_name = 'users'
    ordering = ['-date_joined']