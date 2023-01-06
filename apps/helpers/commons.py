from django.utils.translation import gettext_lazy as _


ADM_IMOB = 'adm_imob_access'
USER_IMOB = 'user_imob_access'

ACCESS_LEVEL_CHOICES = (
    (ADM_IMOB, _('Administrador Imob')),
    (USER_IMOB, _('Usuário Imob')),
)
