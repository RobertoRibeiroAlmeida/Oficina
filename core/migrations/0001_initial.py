# Generated by Django 4.2.6 on 2023-11-13 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GrupoProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cpf', models.CharField(max_length=20)),
                ('celular1', models.CharField(blank=True, max_length=20, null=True)),
                ('celular2', models.CharField(blank=True, max_length=20, null=True)),
                ('especialidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.especialidade')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('unidade', models.CharField(choices=[('UN', 'Unidade'), ('MT', 'Metro linear'), ('M2', 'Metro quadrado'), ('M3', 'Metro cubico'), ('L', 'Litro'), ('KG', 'Quilograma')], max_length=2)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.grupoproduto')),
            ],
        ),
    ]
