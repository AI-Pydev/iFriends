# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'Title')),
                ('text', models.TextField(max_length=204, verbose_name=b'Text')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(default=b'N', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('birthday', models.DateTimeField(verbose_name=b'Birthday')),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email')),
                ('favouriteURL', models.URLField(null=True, verbose_name=b'myURL')),
                ('desc', models.TextField(max_length=500, null=True, verbose_name=b'Desc')),
                ('blogs', models.ManyToManyField(to='Person.Blog', blank=True)),
                ('friends', models.ManyToManyField(related_name='friends_rel_+', to='Person.Person', blank=True)),
            ],
        ),
    ]
