# Generated by Django 3.2.8 on 2022-02-17 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sac',
            old_name='categoria',
            new_name='mensagem',
        ),
    ]
