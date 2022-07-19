# Generated by Django 4.0.5 on 2022-06-28 06:36

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_post_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_about', ckeditor_uploader.fields.RichTextUploadingField(help_text='Полный текст "О блоге". Не может быть пустым. Максимальное количество символов не ограничено.', verbose_name='Полный текст.')),
                ('blog_goals', ckeditor_uploader.fields.RichTextUploadingField(help_text='Полный текст "Цели". Не может быть пустым. Максимальное количество символов не ограничено.', verbose_name='Полный текст.')),
                ('created', models.DateTimeField(verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'О блоге',
                'verbose_name_plural': 'О блоге',
                'ordering': ['-created'],
            },
        ),
    ]