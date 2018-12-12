# Generated by Django 2.0.5 on 2018-12-12 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_taboo_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='TabooList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tWord', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameModel(
            old_name='Complain_OU',
            new_name='ComplainOU',
        ),
        migrations.RenameModel(
            old_name='Taboo_list',
            new_name='PendingTaboo',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='is_OU',
            new_name='isOU',
        ),
        migrations.RenameField(
            model_name='pendingtaboo',
            old_name='t_word',
            new_name='tSubmission',
        ),
    ]
