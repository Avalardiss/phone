# Generated by Django 3.0.4 on 2020-05-02 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abonent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='№ п/п')),
                ('rank', models.CharField(max_length=50, verbose_name='Воинское звание')),
                ('name', models.CharField(max_length=100, verbose_name='Фамилия, Имя, Отчество')),
                ('phone', models.CharField(max_length=10, verbose_name='Рабочий телефон')),
                ('IP_phone', models.CharField(max_length=10, verbose_name='IP телефон')),
            ],
            options={
                'verbose_name': 'Абонент',
            },
        ),
    ]
