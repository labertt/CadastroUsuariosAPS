# Generated by Django 4.1.1 on 2022-10-16 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=256)),
                ('cpf', models.IntegerField(unique=True)),
                ('data_nascimento', models.DateField()),
                ('endereco', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256, unique=True)),
                ('password', models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]