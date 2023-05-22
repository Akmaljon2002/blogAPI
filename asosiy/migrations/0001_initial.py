# Generated by Django 4.2.1 on 2023-05-22 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faoliyat_joy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('rasm', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Hamkor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=50, null=True)),
                ('rasm', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Haqida_toliq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.CharField(blank=True, max_length=50, null=True)),
                ('sarlavhaeng', models.CharField(blank=True, max_length=50, null=True)),
                ('sarlavharu', models.CharField(blank=True, max_length=50, null=True)),
                ('matn', models.TextField(blank=True, null=True)),
                ('matneng', models.TextField(blank=True, null=True)),
                ('matnru', models.TextField(blank=True, null=True)),
                ('rasm', models.FileField(blank=True, null=True, upload_to='')),
                ('hozirgi_orni', models.CharField(blank=True, max_length=200, null=True)),
                ('hozirgi_ornieng', models.CharField(blank=True, max_length=200, null=True)),
                ('hozirgi_orniru', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Home_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(blank=True, max_length=50, null=True)),
                ('ismru', models.CharField(blank=True, max_length=50, null=True)),
                ('matn', models.CharField(blank=True, max_length=60, null=True)),
                ('matneng', models.CharField(blank=True, max_length=60, null=True)),
                ('matnru', models.CharField(blank=True, max_length=60, null=True)),
                ('haqida', models.CharField(blank=True, max_length=20, null=True)),
                ('haqidaeng', models.CharField(blank=True, max_length=20, null=True)),
                ('haqidaru', models.CharField(blank=True, max_length=20, null=True)),
                ('rasm', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Ijtimoiy_tarmoq_url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Maqola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.CharField(blank=True, max_length=100, null=True)),
                ('sarlavhaeng', models.CharField(blank=True, max_length=100, null=True)),
                ('sarlavharu', models.CharField(blank=True, max_length=100, null=True)),
                ('matn', models.TextField(blank=True, null=True)),
                ('matneng', models.TextField(blank=True, null=True)),
                ('matnru', models.TextField(blank=True, null=True)),
                ('sana', models.DateField(auto_now_add=True)),
                ('bosh_sahifa_uchun', models.BooleanField(default=False)),
                ('korilganlik', models.PositiveIntegerField(default=0)),
                ('rasm1', models.FileField(blank=True, null=True, upload_to='')),
                ('rasm2', models.FileField(blank=True, null=True, upload_to='')),
                ('rasm3', models.FileField(blank=True, null=True, upload_to='')),
                ('rasm4', models.FileField(blank=True, null=True, upload_to='')),
                ('rasm5', models.FileField(blank=True, null=True, upload_to='')),
                ('rasm6', models.FileField(blank=True, null=True, upload_to='')),
                ('rasm7', models.FileField(blank=True, null=True, upload_to='')),
                ('rasm8', models.FileField(blank=True, null=True, upload_to='')),
                ('rasm9', models.FileField(blank=True, null=True, upload_to='')),
                ('rasm10', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=30, null=True)),
                ('nomeng', models.CharField(blank=True, max_length=30, null=True)),
                ('nomru', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Murojaat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matn', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.CharField(blank=True, max_length=100, null=True)),
                ('sarlavhaeng', models.CharField(blank=True, max_length=100, null=True)),
                ('sarlavharu', models.CharField(blank=True, max_length=100, null=True)),
                ('matn', models.TextField(blank=True, null=True)),
                ('matneng', models.TextField(blank=True, null=True)),
                ('matnru', models.TextField(blank=True, null=True)),
                ('sana', models.DateField(auto_now_add=True)),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('rasm', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
