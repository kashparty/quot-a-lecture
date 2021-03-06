# Generated by Django 4.0.2 on 2022-02-06 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recording',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panopto_id', models.TextField(unique=True)),
                ('name', models.TextField()),
                ('date', models.DateField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='recordings', to='seapanapp.category')),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='recordings', to='seapanapp.lecturer')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preamble', models.TextField()),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('timestamp', models.TimeField()),
                ('encoding', models.BinaryField()),
                ('votes', models.IntegerField(default=0)),
                ('recording', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='questions', to='seapanapp.recording')),
            ],
        ),
    ]
