# Generated by Django 3.0 on 2019-12-22 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('outdoors', 'Outdoors'), ('entertainment', 'Entertainment'), ('food', 'Food'), ('tech', 'Tech'), ('education', 'Education'), ('health', 'Health')], default='', max_length=100),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Event')),
            ],
        ),
    ]