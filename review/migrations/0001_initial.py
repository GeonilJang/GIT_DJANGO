# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-12 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager', models.CharField(blank=True, help_text='검수자', max_length=10, verbose_name='담당자')),
                ('shopid', models.CharField(blank=True, help_text='가맹점 ID', max_length=20, verbose_name='가맹점 ID')),
                ('shopname', models.CharField(blank=True, help_text='가맹점명', max_length=20, verbose_name='가맹점명')),
                ('shopurl', models.CharField(blank=True, help_text='가맹점URL', max_length=100, verbose_name='가맹점URL')),
                ('hosting', models.CharField(blank=True, help_text='호스팅사', max_length=20, verbose_name='호스팅사')),
                ('server', models.CharField(blank=True, help_text='네임서버', max_length=100, verbose_name='네임서버')),
                ('checklogin', models.CharField(blank=True, default='1.바로구매하기:가능\n2.장바구니:가능', help_text='비회원구매', max_length=100, verbose_name='비회원구매')),
                ('checkcont', models.CharField(blank=True, default='1.상세페이지:특이사항없음\n 2.장바구니:특이사항없음\n 3.옵션기능:특이사항없음', help_text='사이트구조', max_length=100, verbose_name='사이트구조')),
                ('opinion', models.TextField(blank=True, default='상/중/하', help_text='검토의견', verbose_name='검토의견')),
                ('fitness', models.CharField(blank=True, help_text='적합도', max_length=10, verbose_name='적합도')),
                ('dateregi', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
