# Generated by Django 3.2.5 on 2021-07-31 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
        ('characteristic', '0001_initial'),
        ('animal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='characteristic',
        ),
        migrations.AddField(
            model_name='animal',
            name='characteristics',
            field=models.ManyToManyField(related_name='animals', to='characteristic.Characteristic'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animals', to='group.group'),
        ),
    ]
