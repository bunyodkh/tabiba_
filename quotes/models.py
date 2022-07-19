from doctest import BLANKLINE_MARKER
from ssl import create_default_context
from django.db import models
from django.utils.translation import gettext_lazy as _

class Quote(models.Model):
    title = models.TextField(_('Цитата'), null=False, blank=False, help_text=_('Текст цитаты. Максимальное количество символов - 1000.'), max_length=1000)
    author = models.CharField(_('Автор'), null=True, blank=True, help_text=_('Автор цитаты. Максимальное количество символов - 100.'), max_length=100)

    active = models.BooleanField(_('Показать'), default=False)

    created = models.DateTimeField(_('Создано'))
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты'

    def __str__(self) -> str:
        return self.title