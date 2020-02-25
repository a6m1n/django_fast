from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

from app_users import forms, models


class UsersViews(ListView):
    model = models.CustomUser
    context_object_name = "users"
    template_name = "app_users/list.html"
    paginate_by = 2


class UserDetailView(DetailView):
    model = models.CustomUser
    template_name = "app_users/detail.html"
    context_object_name = "user"


class CreateUserView(CreateView):
    template_name = "app_users/create.html"
    form_class = forms.CustomUserCreate
    success_url = "/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        formset = forms.LanguageFormset(queryset=models.Languages.objects.all())

        context["formset"] = formset
        return context


class UserUpdate(UpdateView):
    success_url = "/"
    model = models.CustomUser
    template_name_suffix = "_update"

    form_class = forms.CustomUserCreate


class UserDelete(DeleteView):
    model = models.CustomUser
    template_name_suffix = "_delete"
    success_url = reverse_lazy("list_page")

    def get_object(self):
        new = []

        for k in self.request.POST.keys():
            if k.isnumeric():
                new.append(k)

        return self.model.objects.filter(pk__in=new)
