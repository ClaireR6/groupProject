# Generated by Django 4.0.4 on 2022-05-17 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0003_alter_section_week_days_delete_tatoprofessor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ProjectApp.user'),
        ),
    ]