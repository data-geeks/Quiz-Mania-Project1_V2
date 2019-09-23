# Generated by Django 2.2.5 on 2019-09-21 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='testInfo',
            fields=[
                ('test_id', models.AutoField(primary_key=True, serialize=False)),
                ('test_name', models.CharField(max_length=100)),
                ('test_file', models.CharField(max_length=100)),
                ('Max_score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='testQuestions',
            fields=[
                ('ques_id', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=100)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='userScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TestId', to='TestTime.testInfo')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserId', to='login_register.userInfo')),
            ],
        ),
    ]
