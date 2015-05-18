# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('dob', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
