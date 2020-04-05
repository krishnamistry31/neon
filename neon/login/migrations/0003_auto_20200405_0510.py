# Generated by Django 2.2.11 on 2020-04-05 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20200404_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('subject_code', models.CharField(max_length=10, primary_key='true', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('alias', models.CharField(max_length=30)),
                ('rec_status', models.CharField(max_length=10)),
                ('session', models.IntegerField(default=0)),
                ('elective', models.CharField(max_length=10)),
                ('credit', models.IntegerField(default=0)),
                ('th_min_pass1', models.IntegerField(default=0)),
                ('th_min_pass2', models.IntegerField(default=0)),
                ('th_total', models.IntegerField(default=0)),
                ('sess_min_pass1', models.IntegerField(default=0)),
                ('sess_min_pass3', models.IntegerField(default=0)),
                ('sess_total', models.IntegerField(default=0)),
                ('pr_min_pass1', models.IntegerField(default=0)),
                ('pr_total', models.IntegerField(default=0)),
                ('tw_min_pass1', models.IntegerField(default=0)),
                ('tw_total', models.IntegerField(default=0)),
                ('total_min_pass', models.IntegerField(default=0)),
                ('total_marks', models.IntegerField(default=0)),
                ('syllabus', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('program_code', models.CharField(max_length=10, primary_key='true', serialize=False)),
                ('institute_name', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('alias', models.CharField(max_length=30)),
                ('program_type', models.CharField(max_length=30)),
                ('session_type', models.CharField(max_length=30)),
                ('no_of_sess', models.IntegerField(default=0)),
                ('no_of_year', models.IntegerField(default=0)),
                ('eligibility_criteria', models.CharField(max_length=30)),
                ('result_type', models.CharField(max_length=30)),
                ('total_sessional', models.IntegerField(default=0)),
                ('compulsory_sessional', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='semester',
        ),
        migrations.DeleteModel(
            name='semester',
        ),
        migrations.DeleteModel(
            name='subject',
        ),
        migrations.AddField(
            model_name='course',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Program'),
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(to='login.Course'),
        ),
    ]