# Generated by Django 4.2.2 on 2023-06-27 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=30)),
                ('city', models.CharField(max_length=40)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=30)),
                ('profession', models.CharField(choices=[('Interior Design', 'Interior Design'), ('Architect', 'Architect'), ('Modular Dealer', 'Modular Dealer')], default='Interior Design', max_length=40)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='featured',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='slug',
        ),
        migrations.AlterField(
            model_name='blog',
            name='author_image',
            field=models.ImageField(upload_to='author/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
