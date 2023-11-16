from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .forms import RegistrationUserForm


class RegistrationView(CreateView):
    form_class = RegistrationUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('register_done')


class RegisterDoneView(TemplateView):
    template_name = 'users/register_done.html'
