# Generated by Django 4.2.1 on 2023-05-24 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asosiy', '0002_alter_home_page_matn_alter_home_page_matneng_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='matn',
        ),
        migrations.RemoveField(
            model_name='video',
            name='matneng',
        ),
        migrations.RemoveField(
            model_name='video',
            name='matnru',
        ),
        migrations.RemoveField(
            model_name='video',
            name='sarlavha',
        ),
        migrations.RemoveField(
            model_name='video',
            name='sarlavhaeng',
        ),
        migrations.RemoveField(
            model_name='video',
            name='sarlavharu',
        ),
    ]
