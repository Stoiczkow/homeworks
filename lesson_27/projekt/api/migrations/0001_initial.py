from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Artykul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=200)),
                ('tresc', models.TextField()),
                ('data_dodania', models.DateTimeField(auto_now_add=True)),
                ('data_aktualizacji', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
