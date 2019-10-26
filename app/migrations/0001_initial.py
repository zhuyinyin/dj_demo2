# Generated by Django 2.2.4 on 2019-09-09 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produce',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=32)),
                ('p_describe', models.CharField(max_length=32)),
                ('p_start', models.DateTimeField(auto_now_add=True)),
                ('p_stop', models.DateTimeField(auto_now=True)),
                ('p_price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(default='', max_length=32)),
            ],
        ),
    ]
