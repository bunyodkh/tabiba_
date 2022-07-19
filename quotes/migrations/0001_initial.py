# Generated by Django 4.0.5 on 2022-06-24 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(help_text='Текст цитаты. Максимальное количество символов - 1000.', max_length=1000, verbose_name='Цитата')),
                ('author', models.CharField(blank=True, help_text='Автор цитаты. Максимальное количество символов - 100.', max_length=100, null=True, verbose_name='Автор')),
                ('created', models.DateTimeField(verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Цитата',
                'verbose_name_plural': 'Цитаты',
                'ordering': ['-created'],
            },
        ),
    ]