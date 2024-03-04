from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Advertise
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class ListAds(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'advertise.view_advertise'
    template_name = 'ads/ads-list.html'
    model = Advertise
    context_object_name = 'ads'


class DetailAds(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'advertise.view_advertise'
    template_name = 'ads/ads-detail.html'
    model = Advertise


class DeleteAds(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'advertise.delete_advertise'
    template_name = 'ads/ads-delete.html'
    model = Advertise
    success_url = '/ads/'


class UpdateAds(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'advertise.change_advertise'
    template_name = 'ads/ads-edit.html'
    fields = 'name', 'product', 'budget'
    model = Advertise
    success_url = '/products/'


class CreateAds(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'advertise.add_advertise'
    template_name = 'ads/ads-create.html'
    fields = 'name', 'product', 'budget'
    success_url = '/ads/'
    model = Advertise
