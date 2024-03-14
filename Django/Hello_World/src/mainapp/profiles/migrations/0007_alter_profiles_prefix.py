# Generated by Django 5.0.1 on 2024-02-15 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_profiles_prefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='prefix',
            field=models.CharField(choices=[('Mrs', 'Mrs'), ('Ms', 'Ms'), ('Mr', 'Mr')], default='', max_length=10),
        ),
    ]
