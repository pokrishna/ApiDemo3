# Generated by Django 2.2.3 on 2019-07-31 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('rollno', models.IntegerField()),
                ('marks', models.IntegerField()),
                ('gf', models.CharField(max_length=64)),
                ('bf', models.CharField(max_length=64)),
            ],
        ),
    ]
