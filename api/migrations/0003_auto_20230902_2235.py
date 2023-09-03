# Generated by Django 3.2.4 on 2023-09-03 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_group_id_alter_group_table_activities'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activities',
            old_name='date_activites',
            new_name='date_activities',
        ),
        migrations.RenameField(
            model_name='activities',
            old_name='user',
            new_name='fk_user',
        ),
        migrations.AddField(
            model_name='activities',
            name='color',
            field=models.CharField(db_column='color', default='text-warning', max_length=50),
        ),
    ]
