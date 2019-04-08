# Generated by Django 2.1.7 on 2019-04-06 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20190406_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='permisson',
        ),
        migrations.AddField(
            model_name='customuser',
            name='permission',
            field=models.FileField(blank=True, upload_to='', verbose_name='Разрешения для работы'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='exp',
            field=models.FileField(blank=True, upload_to='', verbose_name='Опыт работы'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='person',
            field=models.CharField(blank=True, choices=[('entity', 'Юридическое лицо'), ('individual', 'Физическое лицо')], max_length=10, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='reviews',
            field=models.FileField(blank=True, upload_to='', verbose_name='Отзывы и рекомендации'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(blank=True, choices=[('custome', 'Заявитель'), ('contractor', 'Подрядчик'), ('staff', 'Сотрудник')], max_length=10, verbose_name='Участник'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='staff',
            field=models.FileField(blank=True, upload_to='', verbose_name='Персонал'),
        ),
    ]