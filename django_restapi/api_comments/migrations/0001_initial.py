# Generated by Django 3.0.3 on 2020-06-08 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('itype', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('ctext', models.TextField()),
            ],
            options={
                'db_table': 'Comments',
            },
        ),
    ]
