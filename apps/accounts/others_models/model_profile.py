from django.db import models
from django.db.models.fields.related import OneToOneField
from django.utils.translation import gettext_lazy as _

from accounts.models import User

class UserProfile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    cpf = models.CharField(verbose_name=_('CPF'), max_length=18, blank=True, null=True)
    state = models.CharField(verbose_name=_('Estado'), max_length=100, blank=True, null=True)
    city = models.CharField(verbose_name=_('Cidade') ,max_length=70, blank=True, null=True)
    number = models.CharField(verbose_name=_('Número da casa') ,max_length=15, blank=True, null=True)
    phone = models.CharField(verbose_name=_('Telefone') ,max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = _('Perfil')
        verbose_name_plural = _('Perfis')

    def get_cpf(self):
        if self.cpf:
            cpf = str(self.cpf)
            cpf_parte_1 = cpf[0:3]
            cpf_parte_2 = cpf[3:6]
            cpf_parte_3 = cpf[6:9]
            cpf_parte_4 = cpf[9:]
            cpf_formatado = f"{cpf_parte_1}.{cpf_parte_2}.{cpf_parte_3}-{cpf_parte_4}"
            return cpf_formatado