# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Padron',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('index', models.BigIntegerField(null=True, blank=True)),
                ('clase', models.TextField(null=True, blank=True)),
                ('apellido', models.TextField(null=True, blank=True)),
                ('sexo', models.TextField(null=True, blank=True)),
                ('primer_nombre', models.TextField(null=True, blank=True)),
                ('segundo_nombre', models.TextField(null=True, blank=True)),
                ('tercer_nombre', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'padron',
                'managed': False,
            },
        ),
    ]
