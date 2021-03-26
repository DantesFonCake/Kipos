# Generated by Django 3.1.5 on 2021-01-23 10:31

import django.contrib.auth.models
import django.db.models.deletion
import jsonfield.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
                name = 'KiposUser',
                fields = [
                    ('id',
                     models.AutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'ID')),
                    ('password', models.CharField(max_length = 128, verbose_name = 'password')),
                    ('last_login', models.DateTimeField(blank = True, null = True, verbose_name = 'last login')),
                    ('username', models.CharField(max_length = 40, unique = True)),
                    ('email', models.EmailField(max_length = 40, unique = True)),
                    ('uuid', models.CharField(max_length = 40, unique = True)),
                ],
                options = {
                    'abstract': False,
                },
                managers = [
                    ('objects', django.contrib.auth.models.UserManager()),
                ],
        ),
        migrations.CreateModel(
                name = 'Module',
                fields = [
                    ('id',
                     models.AutoField(auto_created = True, primary_key = True, serialize = False, verbose_name = 'ID')),
                    ('telemetry', jsonfield.fields.JSONField()),
                    ('user',
                     models.ForeignKey(on_delete = django.db.models.deletion.CASCADE, to = settings.AUTH_USER_MODEL)),
                ],
        ),
    ]
