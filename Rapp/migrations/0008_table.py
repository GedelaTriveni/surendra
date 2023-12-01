# Generated by Django 3.0 on 2023-09-02 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rapp', '0007_remove_slot_usd'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usrname', models.CharField(blank=True, max_length=100, null=True)),
                ('number', models.IntegerField(default=2)),
                ('mobile', models.CharField(blank=True, max_length=10, null=True)),
                ('dateandtime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
