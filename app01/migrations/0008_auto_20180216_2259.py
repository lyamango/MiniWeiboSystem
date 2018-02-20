# Generated by Django 2.0.1 on 2018-02-16 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_auto_20180216_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weibo',
            name='wb_type',
            field=models.IntegerField(choices=[(0, '发布'), (1, '转发'), (2, '收藏')], default=0, verbose_name='微博类型'),
        ),
    ]
