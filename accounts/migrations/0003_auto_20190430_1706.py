# Generated by Django 2.2 on 2019-04-30 08:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190430_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='fullName',
            field=models.CharField(max_length=20, verbose_name='이름'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z0-9]+$')], verbose_name='사용자 아이디'),
        ),
    ]
