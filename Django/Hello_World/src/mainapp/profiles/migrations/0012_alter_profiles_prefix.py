# Generated by Django 5.0.1 on 2024-02-17 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_alter_profiles_prefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='prefix',
            field=models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms')], default='', max_length=10),
        ),
    ]
