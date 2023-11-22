from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView

from .forms import RegistrationUserForm
from main.models import Application


class ProfileView(ListView, LoginRequiredMixin):
    context_object_name = 'applications_list'
    template_name = 'users/profile.html'

    def get_queryset(self):
        return Application.objects.filter(owner=self.request.user)


class ProfileFilterView(ListView, LoginRequiredMixin):
    context_object_name = 'applications_list'
    template_name = 'users/profile.html'

    def get_queryset(self):
        return Application.objects.filter(owner=self.request.user, status=self.request.GET.get('status')[0])


class LoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('profile')


class LogoutView(LogoutView):
    template_name = 'users/logout.html'


class RegistrationView(CreateView):
    form_class = RegistrationUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('register_done')


class RegisterDoneView(TemplateView):
    template_name = 'users/register_done.html'
