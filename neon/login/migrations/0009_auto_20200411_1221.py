# Generated by Django 2.2.11 on 2020-04-11 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_remove_student_courses'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regularresult',
            old_name='extarnal_marks',
            new_name='external_marks',
        ),
    ]
