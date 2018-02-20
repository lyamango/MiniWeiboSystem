# Generated by Django 2.0.1 on 2018-02-17 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_auto_20180216_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='followers',
            field=models.ManyToManyField(blank=True, null=True, related_name='my_watch', to='app01.UserProfile', verbose_name='我的关注'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='follow_list',
            field=models.ManyToManyField(blank=True, related_name='my_fans', to='app01.UserProfile', verbose_name='我的粉丝'),
        ),
    ]
