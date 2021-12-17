# Generated by Django 3.2.8 on 2021-12-03 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('porcao', models.DecimalField(decimal_places=2, max_digits=5)),
                ('valor_calorico', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Nutriente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
                ('sobrenome', models.CharField(max_length=255)),
                ('data_nasc', models.DateField()),
                ('altura', models.DecimalField(decimal_places=2, max_digits=4)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Sac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Refeicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.DateTimeField()),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=6)),
                ('alimento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.alimento')),
            ],
        ),
        migrations.AddField(
            model_name='alimento',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.categoria'),
        ),
        migrations.AddField(
            model_name='alimento',
            name='nutriente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.nutriente'),
        ),
    ]
