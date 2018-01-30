# Generated by Django 2.0.1 on 2018-01-30 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prueba', '0002_auto_20180130_1241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentary',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='favourite',
            name='category_id',
        ),
        migrations.RemoveField(
            model_name='favourite',
            name='user_id',
        ),
        migrations.AddField(
            model_name='commentary',
            name='promotion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prueba.Promotion'),
        ),
        migrations.AddField(
            model_name='commentary',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prueba.User'),
        ),
        migrations.AddField(
            model_name='favourite',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prueba.Category'),
        ),
        migrations.AddField(
            model_name='favourite',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prueba.User'),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prueba.Category'),
        ),
    ]
