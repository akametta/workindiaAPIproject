# Generated by Django 3.1.4 on 2020-12-10 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserFOrm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=60)),
                ('username', models.CharField(max_length=60)),
            ],
        ),
    ]