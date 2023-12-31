# Generated by Django 4.2.7 on 2023-11-05 11:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('days', '0002_word'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studyday',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='word',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='words', to='days.studyday', verbose_name='Day'),
        ),
        migrations.AlterField(
            model_name='word',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='Id'),
        ),
    ]
