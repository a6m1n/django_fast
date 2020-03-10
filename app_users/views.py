"""Classic Django views"""
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

from app_users import forms, models


class ModelUserMixin:
    """Class who have self.model"""
    model = models.CustomUser


class FormSetMixin:
    """Mixin who valid and add to context formset"""
    def form_valid(self, form):
        """formvalid mixin"""
        response = super().form_valid(form)
        formset = forms.LanguageFormset(self.request.POST, instance=self.object)
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return response

    def get_context_data(self, *args, **kwargs):
        """Add to context formset"""
        context = super().get_context_data(*args, **kwargs)
        formset = forms.LanguageFormset(instance=self.object)
        context["formset"] = formset
        return context


class UsersViews(ModelUserMixin, ListView):
    """Classic list views"""
    context_object_name = "users"
    template_name = "app_users/list.html"
    paginate_by = 10


class UserDetailView(ModelUserMixin, DetailView):
    """Classic detail view"""
    template_name = "app_users/detail.html"
    context_object_name = "user"


class CreateUserView(FormSetMixin, CreateView):
    """Classic create view and formsetMixin (check docs formset)"""
    template_name = "app_users/create.html"
    form_class = forms.CustomUserCreate
    success_url = reverse_lazy("list_page")


class UserUpdate(FormSetMixin, ModelUserMixin, UpdateView):
    """Classic update views and form set"""
    success_url = reverse_lazy("list_page")
    template_name_suffix = "_update"
    form_class = forms.CustomUserCreate


class UserDelete(ModelUserMixin, DeleteView):
    """Delete views. Delete one and more objects"""
    template_name_suffix = "_delete"
    success_url = reverse_lazy("list_page")

    def get_object(self):
        """Delete more objects, 1,2,3,4..."""
        new = []
        for k in self.request.POST.keys():
            if k.isnumeric():
                new.append(k)
        return self.model.objects.filter(pk__in=new)
