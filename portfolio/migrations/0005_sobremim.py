# Generated by Django 4.1 on 2022-09-02 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20220826_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='SobreMim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sobre', models.TextField(blank=True)),
                ('mostrar', models.BooleanField(default=False)),
            ],
        ),
    ]
