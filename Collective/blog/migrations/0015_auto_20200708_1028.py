# Generated by Django 3.0.4 on 2020-07-08 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_comment_githubreop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='githubreop',
            field=models.CharField(blank=True, help_text='Supported User/User-Repo', max_length=200, verbose_name='Github repo'),
        ),
    ]
