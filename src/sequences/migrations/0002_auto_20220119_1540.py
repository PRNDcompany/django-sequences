# Generated by Django 3.1.4 on 2022-01-19 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sequences', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sequence',
            name='name',
            field=models.CharField(max_length=300, primary_key=True, serialize=False, verbose_name='name'),
        ),
    ]
