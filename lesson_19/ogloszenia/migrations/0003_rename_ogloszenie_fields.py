# Generated during lesson 19 refactor.

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ogloszenia', '0002_rename_ogłoszenie_ogloszenie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ogloszenie',
            old_name='title',
            new_name='tytul',
        ),
        migrations.RenameField(
            model_name='ogloszenie',
            old_name='description',
            new_name='opis',
        ),
        migrations.RenameField(
            model_name='ogloszenie',
            old_name='price',
            new_name='cena',
        ),
        migrations.RenameField(
            model_name='ogloszenie',
            old_name='created_at',
            new_name='data_dodania',
        ),
    ]
