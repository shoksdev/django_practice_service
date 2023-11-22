from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, CreateView, ListView, UpdateView

from .forms import ApplicationForm, CategoryForm, ApplicationDoneForm, ApplicationInWorkForm
from .models import Application, Category


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


class ApplicationListView(ListView, LoginRequiredMixin):
    context_object_name = 'applications_list'
    template_name = 'main/applications_list.html'

    def get_queryset(self):
        return Application.objects.filter(status='Н')


class ApplicationUpdateStatusDoneView(UpdateView, LoginRequiredMixin):
    model = Application
    form_class = ApplicationDoneForm
    context_object_name = 'application'
    template_name = 'main/application_update_status_done.html'

    def get_queryset(self):
        return Application.objects.filter(status='Н')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.status = 'В'
        instance.save()

        return redirect('applications_list')


class ApplicationUpdateStatusInWorkView(ApplicationUpdateStatusDoneView):
    form_class = ApplicationInWorkForm
    template_name = 'main/application_update_status_inwork.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.status = 'П'
        instance.save()

        return redirect('applications_list')

class CategoryListView(ListView, LoginRequiredMixin):
    model = Category
    context_object_name = 'categories_list'
    template_name = 'main/categories_list.html'


class CategoryCreateView(CreateView, LoginRequiredMixin):
    model = Category
    form_class = CategoryForm
    template_name = 'main/category_create.html'
    success_url = reverse_lazy('categories_list')


@login_required
def category_delete(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect('categories_list')
