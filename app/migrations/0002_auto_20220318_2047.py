# Generated by Django 2.2.22 on 2022-03-18 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='mirriam',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
