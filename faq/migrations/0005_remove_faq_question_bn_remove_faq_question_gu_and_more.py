# Generated by Django 5.1.5 on 2025-02-01 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0004_remove_faq_created_at_remove_faq_updated_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='question_bn',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='question_gu',
        ),
        migrations.RemoveField(
            model_name='faq',
            name='question_hi',
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
    ]
