# Generated by Django 4.0.4 on 2022-05-29 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Familia', '0002_alter_familiares_f_nacimiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sobre_mi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('edad', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=10)),
                ('f_nacimiento', models.DateField(blank=True, null=True)),
            ],
        ),
    ]