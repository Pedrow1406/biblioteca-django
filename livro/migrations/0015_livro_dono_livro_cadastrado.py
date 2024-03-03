# Generated by Django 5.0.2 on 2024-03-03 18:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0014_emprestimo_dono_livro'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='dono_livro_cadastrado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='dono_livro_cadastrado', to='usuarios.usuario'),
            preserve_default=False,
        ),
    ]
