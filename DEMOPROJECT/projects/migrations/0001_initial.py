# Generated by Django 2.2.5 on 2019-09-19 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer_Science',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Software', models.CharField(max_length=250)),
                ('Name', models.CharField(max_length=500)),
                ('Tool', models.CharField(max_length=100)),
                ('Project_Logo', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('University', models.CharField(max_length=500)),
                ('Department', models.CharField(max_length=500)),
                ('Semester', models.CharField(max_length=500)),
                ('Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Computer_Science')),
            ],
        ),
    ]
