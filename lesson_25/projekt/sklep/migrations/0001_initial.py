import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=30)),
                ('nazwisko', models.CharField(max_length=40)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Notatka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=200)),
                ('tresc', models.TextField()),
                ('data_utworzenia', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produkt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=200)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=10)),
                ('opis', models.TextField(blank=True)),
                ('kategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produkty', to='sklep.kategoria')),
            ],
        ),
        migrations.CreateModel(
            name='Ksiazka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=200)),
                ('rok_wydania', models.IntegerField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ksiazki', to='sklep.autor')),
            ],
        ),
    ]
