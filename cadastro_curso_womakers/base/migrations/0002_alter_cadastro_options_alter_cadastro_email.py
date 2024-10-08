# Generated by Django 4.2.16 on 2024-09-18 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cadastro",
            options={
                "ordering": ["-data"],
                "verbose_name": "Formulário de contato",
                "verbose_name_plural": "Formulários de contatos",
            },
        ),
        migrations.AlterField(
            model_name="cadastro",
            name="email",
            field=models.EmailField(max_length=50),
        ),
    ]
