# Generated by Django 4.0.2 on 2022-02-06 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recording',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panopto_id', models.TextField(unique=True)),
                ('name', models.TextField()),
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
                ('votes', models.IntegerField(default=0)),
                ('recording', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='questions', to='seapanapp.recording')),
            ],
        ),
    ]
