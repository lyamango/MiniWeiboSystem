# Generated by Django 2.0.2 on 2018-02-26 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0021_auto_20180226_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='p_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_comments', to='app01.Comment', verbose_name='父级评论'),
        ),
    ]