# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-10-11 05:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageupload', '0007_auto_20181011_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedimage',
            name='bs_thename',
            field=models.CharField(default='지역명', max_length=255, verbose_name='location name'),
        ),
        migrations.AlterField(
            model_name='uploadedimage',
            name='bs_title',
            field=models.CharField(default='소개 타이틀', max_length=255, verbose_name='Title of intro image'),
        ),
        migrations.AlterField(
            model_name='uploadedimage',
            name='bs_writer',
            field=models.CharField(default='소개 작가', max_length=255, verbose_name='writer of intro image'),
        ),
    ]