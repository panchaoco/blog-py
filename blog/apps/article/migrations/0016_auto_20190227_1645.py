# Generated by Django 2.1.4 on 2019-02-27 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_auto_20190225_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticle',
            name='category_type',
            field=models.CharField(blank=True, help_text='文章分类', max_length=100, null=True, verbose_name='文章分类'),
        ),
    ]
