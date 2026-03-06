# Generated migration: add email to PriseDeContact, rename Localisation fields

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prisedecontact',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254),
            preserve_default=True,
        ),
        migrations.RenameField(
            model_name='localisation',
            old_name='lattitde',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='localisation',
            old_name='Quartier',
            new_name='quartier',
        ),
    ]
