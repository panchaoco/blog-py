# Generated by Django 2.1.4 on 2019-01-30 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20190130_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogarticle',
            name='comment',
        ),
        migrations.AddField(
            model_name='blogarticle',
            name='comment_count',
            field=models.IntegerField(blank=True, default=10, help_text='评论条数', null=True, verbose_name='评论条数'),
        ),
    ]
