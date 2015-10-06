# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Fisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(to='pessoa.Pessoa', serialize=False, auto_created=True, primary_key=True, parent_link=True)),
                ('sobrenome', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('pessoa.pessoa',),
        ),
        migrations.CreateModel(
            name='Juridica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(to='pessoa.Pessoa', serialize=False, auto_created=True, primary_key=True, parent_link=True)),
                ('razao_social', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
            bases=('pessoa.pessoa',),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='polymorphic_ctype',
            field=models.ForeignKey(null=True, related_name='polymorphic_pessoa.pessoa_set+', to='contenttypes.ContentType', editable=False),
        ),
        migrations.AddField(
            model_name='participante',
            name='pessoa',
            field=models.ForeignKey(to='pessoa.Pessoa'),
        ),
    ]
