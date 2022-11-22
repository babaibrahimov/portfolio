# Generated by Django 4.1.3 on 2022-11-20 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('responsive', models.BooleanField(default=True)),
            ],
        ),
    ]
