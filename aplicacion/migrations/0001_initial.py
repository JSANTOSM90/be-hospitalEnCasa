# Generated by Django 3.0 on 2022-09-23 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='paciente',
            fields=[
                ('id_paciente', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('cc', models.CharField(max_length=40)),
            ],
        ),
    ]
