# Generated by Django 4.2.1 on 2023-05-28 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(max_length=20)),
                ('second_name', models.TextField(max_length=20)),
                ('last_name', models.TextField(max_length=20)),
                ('birth_date', models.DateField(auto_now_add=True)),
                ('adress', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.FloatField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='petclinic.client')),
            ],
        ),
    ]
