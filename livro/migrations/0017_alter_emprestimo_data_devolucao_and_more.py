# Generated by Django 5.0.2 on 2024-03-04 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0016_remove_emprestimo_dono_livro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='data_devolucao',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='data_emprestimo',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]