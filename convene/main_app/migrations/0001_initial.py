# Generated by Django 2.2.6 on 2020-01-02 19:15

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('date', models.DateField(verbose_name='event date')),
                ('time', models.TimeField(verbose_name='event time')),
                ('location', models.CharField(max_length=100)),
                ('capacity', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=250), size=None)),
                ('infolink', models.CharField(max_length=1000)),
                ('is_attending', models.NullBooleanField(default=None)),
                ('description', models.TextField(max_length=2000)),
                ('category', models.CharField(choices=[('outdoors', 'Outdoors'), ('entertainment', 'Entertainment'), ('food', 'Food'), ('tech', 'Tech'), ('education', 'Education'), ('health', 'Health')], default='', max_length=100)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_attending', models.NullBooleanField(default=False)),
                ('event', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='guests', to='main_app.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main_app.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]