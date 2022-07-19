from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from helpers.utils import path_and_rename


class Page(models.Model):
    slug = models.SlugField(_('Ссылка на страницу'), max_length=100, null=False, blank=False, help_text=_('Ссылка на страницу. Не может быть пустым. Максимальное количество символов 100.'))
    title = models.CharField(_('Заголовок'), max_length=500, null=False, blank=False, help_text=_('Заголовок страницы. Не может быть пустым. Максимальное количество символов 500.'))
    full_content = RichTextUploadingField(_('Полный текст статьи'), null=False, blank=False, help_text=_('Полный текст статьи. Не может быть пустым. Максимальное количество символов не ограничено.'))
    draft = models.BooleanField(_('Черновик'), default=False, help_text=_('Отметить как черновик. Не будет показываться пользователям.'))

    created = models.DateTimeField(_('Создано'))
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def get_absolute_url(self, **kwargs):
        return reverse('pages:page-detail', kwargs={'pk': self.id})

    def get_static_url(self, **kwargs):
        return self.slug

    def __str__(self) -> str:
        return self.title