# Generated by Django 3.2.3 on 2021-05-17 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Investments',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('plan', models.CharField(max_length=1000)),
                ('amount', models.CharField(max_length=1000)),
                ('investor', models.CharField(max_length=1000)),
                ('phone', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=1000)),
                ('start', models.CharField(max_length=1000)),
                ('end', models.CharField(max_length=1000)),
                ('roi', models.CharField(max_length=1000)),
                ('status', models.CharField(max_length=1000)),
                ('unit', models.IntegerField()),
                ('address', models.CharField(max_length=1000)),
                ('fullname', models.CharField(max_length=1000)),
                ('day', models.CharField(max_length=1000)),
                ('platform', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'investment',
                'verbose_name_plural': 'investments',
                'db_table': 'investments',
            },
        ),
    ]