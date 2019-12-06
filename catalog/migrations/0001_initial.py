# Generated by Django 3.0 on 2019-12-06 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='ModelQuantidadeFatias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_de_fatias', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'quantidade de fatias',
                'verbose_name_plural': 'quantidade de fatias',
            },
        ),
        migrations.CreateModel(
            name='ModelDoces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('preco', models.PositiveIntegerField(null=True)),
                ('descricao', models.TextField(max_length=200, null=True)),
                ('imagem', models.ImageField(null=True, upload_to='imagens_de_doces')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.ModelCategoria')),
                ('quantidade_de_fatias', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.ModelQuantidadeFatias')),
            ],
            options={
                'verbose_name': 'doce',
                'verbose_name_plural': 'doces',
            },
        ),
    ]
