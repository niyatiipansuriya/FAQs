# Generated by Django 5.1.5 on 2025-02-01 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            'faq',
            '0007_remove_faq_is_bn_enabled_remove_faq_is_gu_enabled_and_more'
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='question_en',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='question_gu',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='question_mr',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='question_ta',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='question_te',
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_bn',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_hi',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_bn',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_hi',
            field=models.TextField(blank=True, null=True),
        ),
    ]
