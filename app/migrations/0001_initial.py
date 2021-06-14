# Generated by Django 3.2.4 on 2021-06-14 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('photoURL', models.TextField()),
                ('password', models.TextField()),
                ('salt', models.TextField()),
            ],
        ),
    ]
