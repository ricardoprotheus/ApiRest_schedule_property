from functools import wraps
from django.contrib import messages
from django.utils.translation import gettext as _
from django.shortcuts import redirect

from helpers import commons
from accounts.others_models.model_user_clinic import UserClinic
from accounts.models import User


def admin_level_required(view_func):
    def _decorator(request, *args, **kwargs):
        try:
            user_clinic_permission = UserClinic.objects.get(user=request.user, user__is_active=True)
        except UserClinic.DoesNotExist:
            user_clinic_permission = UserClinic.objects.filter(user=request.user, user__is_active=True).first() #, is_active=True
            user_clinic_permission.user.is_active = True
            user_clinic_permission.save()
        if user_clinic_permission.user.role == commons.ADM_CLIPSE or user_clinic_permission.user.role == commons.ADM_CLINIC:
            response = view_func(request, *args, **kwargs)
            return response
        else:
            messages.warning(request, _('Você não tem permissão pra acessar o recurso'))
            return redirect('home')
    return wraps(view_func)(_decorator)

def admin_clipse_level_required(view_func):
    def _decorator(request, *args, **kwargs):
        try:
            user_clinic_permission = UserClinic.objects.get(user=request.user, user__is_active=True)
        except UserClinic.DoesNotExist:
            user_clinic_permission = UserClinic.objects.filter(user=request.user, user__is_active=True).first()
            user_clinic_permission.user.is_active = True
            user_clinic_permission.save()
        if user_clinic_permission.user.role == commons.ADM_CLIPSE or user_clinic_permission.user.is_superuser or user_clinic_permission.user.user_clipse:
            response = view_func(request, *args, **kwargs)
            return response
        else:
            messages.warning(request, _('Você não tem permissão pra acessar o recurso.'))
            return redirect('home')
    return wraps(view_func)(_decorator)

def customer_level_required(view_func):
    def _decorator(request, *args, **kwargs):
        try:
            user_clinic_permission = UserClinic.objects.get(user=request.user, user__is_active=True)
        except UserClinic.DoesNotExist:
            user_clinic_permission = UserClinic.objects.filter(user=request.user, user__is_active=True).first()
            user_clinic_permission.user.is_active = True
            user_clinic_permission.save()
        if user_clinic_permission.user == commons.ADM_CLIPSE or user_clinic_permission.user == commons.ADM_CLINIC or user_clinic_permission.user == commons.USER_CLIPSE or user_clinic_permission.user == commons.USER_CLINIC or request.user.is_superuser:
            response = view_func(request, *args, **kwargs)
            return response
        else:
            messages.warning(request, _('Você não tem permissão pra acessar o recurso.'))
            return redirect('home')
    return wraps(view_func)(_decorator)
    