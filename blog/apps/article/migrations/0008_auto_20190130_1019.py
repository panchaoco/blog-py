# Generated by Django 2.1.4 on 2019-01-30 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20190130_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticle',
            name='comment',
            field=models.ForeignKey(blank=True, help_text='评论', null=True, on_delete=django.db.models.deletion.CASCADE, to='comment.Comment', to_field='article_id', verbose_name='评论'),
        ),
    ]
