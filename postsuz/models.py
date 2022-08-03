from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from helpers.utils import path_and_rename


class PostUz(models.Model):
    title = models.CharField(_('Мақоланинг сарлавҳаси'), max_length=500, null=False, blank=False, help_text=_('Заголовок статьи. Не может быть пустым. Максимальное количество символов 500.'))
    main_image = models.ImageField(_('Асосий расм'), upload_to=path_and_rename('uploads/spotlight'), null=True, blank=True)
    main_image_caption = models.CharField(_('Асосий расмга изоҳ'), max_length=500, null=True, blank=True, help_text=_('Максимальное количество символов 500.'))
    brief = models.TextField(_('Мақоланиниг қисқа матн'), max_length=2000, null=True, blank=True, help_text=_('Краткое описание статьи. Будет показыватсья в списках вместе с картинкой. Максимальное количество символов 500.'))
    full_content = RichTextUploadingField(_('Мақоланинг тўлиқ матни'), null=False, blank=False, help_text=_('Полный текст статьи. Не может быть пустым. Максимальное количество символов не ограничено.'))
    draft = models.BooleanField(_('Қоралама'), default=False, help_text=_('Отметить как черновик. Не будет показываться пользователям.'))
    main = models.BooleanField(_('Асосий мақола'), default=False, help_text=_('Отметить как основную статью на главной странице.'))
    category = models.ForeignKey('CategoryUz', on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Категория')
    themes = models.ManyToManyField('ThemeUz', verbose_name='Мавзулар')


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
    blog_intro = RichTextUploadingField(_('"Салом" тўлиқ матни'), null=False, blank=False, help_text=_('"Саломлашиш" тўлиқ матни. Бўш бўлиши мумкин эмас. [em] элементи учун класс номи "em"'))
    blog_about = RichTextUploadingField(_('"Блог ҳақида" тўлиқ матни'), null=False, blank=False, help_text=_('"Блог ҳақида" тўлиқ матни. Бўш бўлиши мумкин эмас. [p] элементи учун класс номи "about-text"'))
    blog_goals = RichTextUploadingField(_('"Бизнинг мақсадимиз" тўлиқ матни'), null=False, blank=False, help_text=_('"Бизнинг мақсадимиз". тўлиқ матни. Бўш бўлиши мумкин эмас. [p] элементи учун класс номи "about-text"'))

    created = models.DateTimeField(_('Яратилди'))
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Блог ҳақида'
        verbose_name_plural = 'Блог ҳақида'

    def __str__(self) -> str:
        return '"Блог ҳақида" блокининг матни' + f' - ({self.created} да яратилди.)'



class CategoryUz(models.Model):
    title = models.CharField(_('Категория'), max_length=50, null=False, blank=False, help_text=_('Категория номи. Бўш бўлиши мумкин эмас. Белгиларнинг максимал сони 50.'))
    number = models.PositiveIntegerField(_('Тартиб рақами'), help_text=_('Рақам саралаш учун керак. Мисол учун, агар қиймат [0] бўлса, тоифа рўйхатда биринчи бўлиб кўрсатилади.'), null=False, blank=False, default=0)
    
    class Meta:
        ordering = ['number']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категориялар'

    def __str__(self) -> str:
        return self.title

    def get_slug(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('postsuz:categoryuz-detail', kwargs={'pk': self.id})



class ThemeUz(models.Model):
    title = models.CharField(_('Мавзу'), max_length=30, null=False, blank=False, help_text=_('Мавзу номи. Бўш бўлиши мумкин эмас. Белгиларнинг максимал сони 30.'))
    slug = models.SlugField(auto_created=True, null=True, blank=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Мавзу'
        verbose_name_plural = 'Мавзулар'

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('postsuz:themeuz-detail', kwargs={'pk': self.id})

