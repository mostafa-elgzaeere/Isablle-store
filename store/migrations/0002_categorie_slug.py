# Generated by Django 3.2.4 on 2021-06-29 12:07

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=' ', editable=False, populate_from='name'),
        ),
    ]