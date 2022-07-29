from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from helpers.utils import path_and_rename


class Post(models.Model):
    title = models.CharField(_('Заголовок'), max_length=500, null=False, blank=False, help_text=_('Заголовок статьи. Не может быть пустым. Максимальное количество символов 500.'))
    main_image = models.ImageField(_('Главное изображению'), upload_to=path_and_rename('uploads/spotlight'), null=True, blank=True)
    main_image_caption = models.CharField(_('Подпись к изображению'), max_length=500, null=True, blank=True, help_text=_('Максимальное количество символов 500.'))
    brief = models.TextField(_('Краткое описание'), max_length=2000, null=True, blank=True, help_text=_('Краткое описание статьи. Будет показыватсья в списках вместе с картинкой. Максимальное количество символов 500.'))
    full_content = RichTextUploadingField(_('Полный текст статьи'), null=False, blank=False, help_text=_('Полный текст статьи. Не может быть пустым. Максимальное количество символов не ограничено.'))
    draft = models.BooleanField(_('Черновик'), default=False, help_text=_('Отметить как черновик. Не будет показываться пользователям.'))
    main = models.BooleanField(_('Освновная статья'), default=False, help_text=_('Отметить как основную статью на главной странице.'))
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Категория')
    themes = models.ManyToManyField('Theme', verbose_name='Темы')


    created = models.DateTimeField(_('Создано'))
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def get_absolute_url(self, **kwargs):
        return reverse('posts:post-detail', kwargs={'pk': self.id})

    def get_static_url(self, **kwargs):
        return self.slug

    def __str__(self) -> str:
        return self.title


class About(models.Model):
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


class Category(models.Model):
    title = models.CharField(_('Категория'), max_length=50, null=False, blank=False, help_text=_('Название категории. Не может быть пустым. Максимальное количество символов 50.'))
    number = models.PositiveIntegerField(_('Порядковый номер'), help_text=_('Номер нужен для сортировки. Например, если значение [0] категория будет отображаться первым в списке.'), null=False, blank=False, default=0)
    
    class Meta:
        ordering = ['number']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.title

    def get_slug(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('posts:category-detail', kwargs={'pk': self.id})



class Theme(models.Model):
    title = models.CharField(_('Тема'), max_length=30, null=False, blank=False, help_text=_('Название темы. Не может быть пустым. Максимальное количество символов 30.'))
    slug = models.SlugField(auto_created=True, null=True, blank=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('posts:theme-detail', kwargs={'pk': self.id})



