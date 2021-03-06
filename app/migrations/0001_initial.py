# Generated by Django 2.2.22 on 2022-03-18 20:40

from django.db import migrations, models
import tabnanny


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nairobi', models.CharField(max_length=30, null=True)),
                ('thika', models.CharField(max_length=200, null=True)),
                ('kisumu', models.CharField(blank=True, max_length=30, null=True)),
                ('mombasa', models.CharField(blank=True, max_length=30, null=True)),
                ('nyeri', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brookside', models.BooleanField(verbose_name=True)),
                ('broadways', models.BooleanField(verbose_name=True)),
                ('safaricom', models.BooleanField(verbose_name=True)),
                ('toilex', models.BooleanField(verbose_name=True)),
                ('bic', models.BooleanField(verbose_name=True)),
                ('nuru_gas', models.BooleanField(verbose_name=True)),
                ('ludan', models.BooleanField(verbose_name=tabnanny.check)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, max_length=20, null=True)),
                ('price', models.CharField(blank=True, max_length=30, null=True)),
                ('vat', models.IntegerField()),
                ('offer', models.IntegerField()),
                ('deliverly', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kiashShop', models.CharField(max_length=200, null=True)),
                ('nomsShop', models.CharField(blank=True, max_length=255, null=True)),
                ('Snaveshop', models.CharField(blank=True, max_length=200, null=True)),
                ('mirriam', models.TextField(blank=True, max_length=45, null=True)),
                ('maathais', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Workerdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=300, null=True)),
                ('middlename', models.CharField(max_length=200, null=True)),
                ('lastname', models.CharField(max_length=30, null=True)),
                ('phone_number', models.IntegerField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(blank=True, max_length=200, null=True)),
                ('position', models.CharField(blank=True, max_length=30, null=True)),
                ('home_place', models.CharField(max_length=200, null=True)),
                ('medical_effects', models.CharField(blank=True, max_length=200, null=30)),
                ('companies', models.ForeignKey(on_delete=True, to='app.Companies')),
            ],
        ),
        migrations.CreateModel(
            name='SuperheadQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maathais', models.CharField(blank=True, max_length=200, null=True)),
                ('Magunas', models.CharField(max_length=200, null=True)),
                ('Tuskeys', models.CharField(blank=True, max_length=40, null=True)),
                ('Leestar', models.CharField(max_length=200, null=True)),
                ('all', models.ForeignKey(on_delete=True, to='app.Shop')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('milk', models.CharField(blank=True, max_length=200, null=True)),
                ('cake', models.CharField(max_length=300, null=True)),
                ('credit', models.IntegerField()),
                ('tissue', models.CharField(blank=True, max_length=200, null=True)),
                ('pen', models.CharField(blank=True, max_length=20, null=True)),
                ('books', models.CharField(max_length=100, null=True)),
                ('gas', models.CharField(blank=True, max_length=200, null=True)),
                ('bulb', models.CharField(max_length=20)),
                ('product', models.ForeignKey(on_delete=True, to='app.Shop')),
            ],
        ),
        migrations.CreateModel(
            name='HeadQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usa', models.CharField(max_length=200, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('travel_cost', models.IntegerField()),
                ('ameriaca', models.ForeignKey(on_delete=True, to='app.Area')),
                ('kenya', models.ForeignKey(null=True, on_delete='cascade', to='app.Shop')),
            ],
        ),
        migrations.AddField(
            model_name='companies',
            name='products',
            field=models.ForeignKey(on_delete=True, to='app.Products'),
        ),
        migrations.AddField(
            model_name='area',
            name='places',
            field=models.ForeignKey(on_delete='cascade', to='app.Shop'),
        ),
    ]
