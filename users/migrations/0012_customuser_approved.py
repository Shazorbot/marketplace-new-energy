# Generated by Django 2.1.7 on 2019-04-06 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_customuser_equip'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='Подтверждённый пользователь'),
        ),
    ]