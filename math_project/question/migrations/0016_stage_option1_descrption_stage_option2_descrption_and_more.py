# Generated by Django 5.0.6 on 2024-09-25 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0015_alter_question_img_base64'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='option1_descrption',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stage',
            name='option2_descrption',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stage',
            name='option3_descrption',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stage',
            name='option4_descrption',
            field=models.TextField(blank=True, null=True),
        ),
    ]
