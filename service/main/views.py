from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, CreateView

from .forms import ApplicationForm
from .models import Application


def index(request):
    applications_list = Application.objects.filter(status='В')[:4]
    applications_counter = Application.objects.filter(status='П').count()
    return render(
        request, 'main/index.html', {
            'applications_list': applications_list, 'applications_counter': applications_counter}
    )


class ApplicationCreateView(CreateView, LoginRequiredMixin):
    model = Application
    form_class = ApplicationForm
    template_name = 'main/application_create.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        instance.save()

        return redirect('profile')


class ApplicationDeleteView(DeleteView, LoginRequiredMixin):
    model = Application
    context_object_name = 'application'
    success_url = reverse_lazy('profile')
