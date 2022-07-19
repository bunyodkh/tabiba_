from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from helpers.utils import path_and_rename

from posts.models import Category, Theme

class PostUz(models.Model):
    title = models.CharField(_('Мақоланинг сарлавҳаси'), max_length=500, null=False, blank=False, help_text=_('Заголовок статьи. Не может быть пустым. Максимальное количество символов 500.'))
    main_image = models.ImageField(_('Асосий расм'), upload_to=path_and_rename('uploads/spotlight'), null=True, blank=True)
    main_image_caption = models.CharField(_('Асосий расмга изоҳ'), max_length=500, null=True, blank=True, help_text=_('Максимальное количество символов 500.'))
    brief = models.TextField(_('Мақоланиниг қисқа матн'), max_length=2000, null=True, blank=True, help_text=_('Краткое описание статьи. Будет показыватсья в списках вместе с картинкой. Максимальное количество символов 500.'))
    full_content = RichTextUploadingField(_('Мақоланинг тўлиқ матни'), null=False, blank=False, help_text=_('Полный текст статьи. Не может быть пустым. Максимальное количество символов не ограничено.'))
    draft = models.BooleanField(_('Қоралама'), default=False, help_text=_('Отметить как черновик. Не будет показываться пользователям.'))
    main = models.BooleanField(_('Асосий мақола'), default=False, help_text=_('Отметить как основную статью на главной странице.'))
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Категория')
    themes = models.ManyToManyField(Theme, verbose_name='Мавзулар')


    created = models.DateTimeField(_('Яратилган вақт'))
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Мақола'
        verbose_name_plural = 'Мақолалар'

    def get_absolute_url(self, **kwargs):
        return reverse('postuz:post-detail', kwargs={'pk': self.id})

    def get_static_url(self, **kwargs):
        return self.slug

    def __str__(self) -> str:
        return self.title


class AboutUz(models.Model):
    blog_intro = RichTextUploadingField(_('Полный текст "Приветствие"'), null=False, blank=False, help_text=_('Полный текст "Приветствие". Не может быть пустым. Класс для [em] элемента "em"'))
    blog_about = RichTextUploadingField(_('Полный текст "О блоге"'), null=False, blank=False, help_text=_('Полный текст "О блоге". Не может быть пустым. Класс для [p] элемента "about-text"'))
    blog_goals = RichTextUploadingField(_('Полный текст "Наша цель"'), null=False, blank=False, help_text=_('Полный текст "Наша цель". Не может быть пустым. Класс для [p] элемента "about-text"'))

    created = models.DateTimeField(_('Создано'))
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'О блоге'
        verbose_name_plural = 'О блоге'

    def __str__(self) -> str:
        return 'Текст для блока "О блоге"' + f' - (создано в {self.created})'



