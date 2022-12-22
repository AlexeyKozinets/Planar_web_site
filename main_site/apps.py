from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MainSiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_site'
    verbose_name = _('Компании и оборудование')
